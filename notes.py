import mcschematic as mcs
schem = mcs.MCSchematic()

#i cant think of a better way to place a block with a custom note lol
def placenote(n, nx, ny, nz):
    match n:
        case 0:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=0]")
        case 1:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=1]")
        case 2:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=2]")
        case 3:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=3]")
        case 4:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=4]")
        case 5:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=5]")
        case 6:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=6]") 
        case 7:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=7]")
        case 8:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=8]")
        case 9:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=9]")
        case 10:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=10]")
        case 11:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=11]")
        case 12:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=12]")
        case 13:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=13]")
        case 14:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=14]")
        case 15:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=15]")
        case 16:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=16]")
        case 17:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=17]")
        case 18:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=18]")
        case 19:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=19]")
        case 20:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=20]")
        case 21:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=21]")
        case 22:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=22]")
        case 23:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=23]")
        case 24:
            schem.setBlock((nx, ny, nz), "minecraft:note_block[note=24]")

def placerest(r,rx,ry,rz):
    match r:
        case 1:
            schem.setBlock((rx, ry, rz), "minecraft:repeater[delay=1,facing=west]")
            schem.setBlock((rx,ry-1,rz),"minecraft:smooth_stone")
        case 2:
            schem.setBlock((rx, ry, rz), "minecraft:repeater[delay=2,facing=west]")
            schem.setBlock((rx,ry-1,rz),"minecraft:smooth_stone")
        case 3:
            schem.setBlock((rx, ry, rz), "minecraft:repeater[delay=3,facing=west]")
            schem.setBlock((rx,ry-1,rz),"minecraft:smooth_stone")
        case 4:
            schem.setBlock((rx, ry, rz), "minecraft:repeater[delay=4,facing=west]")
            schem.setBlock((rx,ry-1,rz),"minecraft:smooth_stone")



#the list of notes and length of delay on repeaters (aka the only thing you have to change to make a song)
notes=[22,17,18,20,18,17,15,15,18,22,20,18,17,17,18,20,22,18,15,15]
rests=[8,4,4,8,4,4,8,4,4,8,4,4,8,4,4,8,8,8,8,16]




pos=0
for i in range(0,len(notes)-1):
    placenote(notes[i],pos,0,0)
    if (rests[i]<=4):
        placerest(rests[i],pos+1,0,0)
        pos+=2
    else:
        while(rests[i]>4):
            placerest(4,pos+1,0,0)
            pos+=1
            rests[i]-=4
        placerest(rests[i],pos+1,0,0)
        pos+=2
placenote(notes[i+1],pos,0,0)




schem.save("/home/jan-aki/.minecraft/config/worldedit/schematics", "song", mcs.Version.JE_1_20_1)
