import MyGame.Sample.Monster as Monster

buf = open('output_monster.bin', 'rb').read()
buf = bytearray(buf)
monster = Monster.Monster.GetRootAsMonster(buf, 0)
hp = monster.Hp()
pos = monster.Pos()

print(hp, pos)