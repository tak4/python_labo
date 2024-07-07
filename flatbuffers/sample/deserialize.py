import MyGame.Sample.Color
import MyGame.Sample.Equipment
import MyGame.Sample.Monster
import MyGame.Sample.Vec3
import MyGame.Sample.Weapon

# Example of how to use FlatBuffers to create and read binary buffers.

def main():

    with open('output_monster.bin', 'rb') as f:
        buf = f.read()
        buf = bytearray(buf)

    # Note: We use `0` for the offset here, since we got the data using the
    # `builder.Output()` method. This simulates the data you would store/receive
    # in your FlatBuffer. If you wanted to read from the `builder.Bytes` directly,
    # you would need to pass in the offset of `builder.Head()`, as the builder
    # actually constructs the buffer backwards.
    monster = MyGame.Sample.Monster.Monster.GetRootAsMonster(buf, 0)

    # Note: We did not set the `Mana` field explicitly, so we get a default value.
    assert monster.Mana() == 150
    assert monster.Hp() == 300
    assert monster.Name() == b'Orc'
    assert monster.Color() == MyGame.Sample.Color.Color().Red
    assert monster.Pos().X() == 1.0
    assert monster.Pos().Y() == 2.0
    assert monster.Pos().Z() == 3.0

    # Get and test the `inventory` FlatBuffer `vector`.
    for i in range(monster.InventoryLength()):
        assert monster.Inventory(i) == i

    # Get and test the `weapons` FlatBuffer `vector` of `table`s.
    expected_weapon_names = [b'Sword', b'Axe']
    expected_weapon_damages = [3, 5]
    for i in range(monster.WeaponsLength()):
        assert monster.Weapons(i).Name() == expected_weapon_names[i]
        assert monster.Weapons(i).Damage() == expected_weapon_damages[i]

    # Get and test the `equipped` FlatBuffer `union`.
    assert monster.EquippedType() == MyGame.Sample.Equipment.Equipment().Weapon

    # An example of how you can appropriately convert the table depending on the
    # FlatBuffer `union` type. You could add `elif` and `else` clauses to handle
    # the other FlatBuffer `union` types for this field.
    if monster.EquippedType() == MyGame.Sample.Equipment.Equipment().Weapon:
        # `monster.Equipped()` returns a `flatbuffers.Table`, which can be used
        # to initialize a `MyGame.Sample.Weapon.Weapon()`, in this case.
        union_weapon = MyGame.Sample.Weapon.Weapon()
        union_weapon.Init(monster.Equipped().Bytes, monster.Equipped().Pos)

        assert union_weapon.Name() == b"Axe"
        assert union_weapon.Damage() == 5

    print('The FlatBuffer was successfully created and verified!')

if __name__ == '__main__':
  main()
