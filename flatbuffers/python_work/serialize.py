import flatbuffers
import MyGame.Sample.Monster as Monster
import MyGame.Sample.Vec3 as Vec3

# Create a FlatBuffer Builder
builder = flatbuffers.Builder(0)

# Create a Vec3 object
Monster.MonsterStart(builder)
Monster.MonsterAddPos(builder, Vec3.CreateVec3(builder, 1.0, 2.0, 3.0))
Monster.MonsterAddMana(builder, 150)
Monster.MonsterAddHp(builder, 100)
# Monster.MonsterAddName(builder, builder.CreateString("Monster"))
# Monster.MonsterAddColor(builder, Monster.Color.Red)
Monster.MonsterAddInventory(builder, False)
monster = Monster.MonsterEnd(builder)

# Finish building the buffer
builder.Finish(monster)

# Output the buffer data
buf = builder.Output()

# Write the binary data to a file
with open('output_monster.bin', 'wb') as f:
   f.write(buf)