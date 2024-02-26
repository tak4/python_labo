import flatbuffers
import MyGame.Sample.Color
import MyGame.Sample.Equipment
import MyGame.Sample.Monster
import MyGame.Sample.Vec3
import MyGame.Sample.Weapon

# Example of how to use FlatBuffers to create and read binary buffers.

def main():
    builder = flatbuffers.Builder(0)

    # Create some weapons for our Monster ('Sword' and 'Axe').
    weapon_one = builder.CreateString('Sword')
    weapon_two = builder.CreateString('Axe')

    MyGame.Sample.Weapon.WeaponStart(builder)
    MyGame.Sample.Weapon.WeaponAddName(builder, weapon_one)
    MyGame.Sample.Weapon.WeaponAddDamage(builder, 3)
    sword = MyGame.Sample.Weapon.WeaponEnd(builder)

    MyGame.Sample.Weapon.WeaponStart(builder)
    MyGame.Sample.Weapon.WeaponAddName(builder, weapon_two)
    MyGame.Sample.Weapon.WeaponAddDamage(builder, 5)
    axe = MyGame.Sample.Weapon.WeaponEnd(builder)

    # Serialize the FlatBuffer data.
    name = builder.CreateString('Orc')

    MyGame.Sample.Monster.MonsterStartInventoryVector(builder, 10)
    # Note: Since we prepend the bytes, this loop iterates in reverse order.
    for i in reversed(range(0, 10)):
        builder.PrependByte(i)
    inv = builder.EndVector()

    MyGame.Sample.Monster.MonsterStartWeaponsVector(builder, 2)
    # Note: Since we prepend the data, prepend the weapons in reverse order.
    builder.PrependUOffsetTRelative(axe)
    builder.PrependUOffsetTRelative(sword)
    weapons = builder.EndVector()

    pos = MyGame.Sample.Vec3.CreateVec3(builder, 1.0, 2.0, 3.0)

    MyGame.Sample.Monster.MonsterStart(builder)
    MyGame.Sample.Monster.MonsterAddPos(builder, pos)
    MyGame.Sample.Monster.MonsterAddHp(builder, 300)
    MyGame.Sample.Monster.MonsterAddName(builder, name)
    MyGame.Sample.Monster.MonsterAddInventory(builder, inv)
    MyGame.Sample.Monster.MonsterAddColor(builder,
                                        MyGame.Sample.Color.Color().Red)
    MyGame.Sample.Monster.MonsterAddWeapons(builder, weapons)
    MyGame.Sample.Monster.MonsterAddEquippedType(
        builder, MyGame.Sample.Equipment.Equipment().Weapon)
    MyGame.Sample.Monster.MonsterAddEquipped(builder, axe)
    orc = MyGame.Sample.Monster.MonsterEnd(builder)

    builder.Finish(orc)

    # Output the buffer data
    buf = builder.Output()

    # Write the binary data to a file
    with open('output_monster.bin', 'wb') as f:
        f.write(buf)


if __name__ == '__main__':
  main()
