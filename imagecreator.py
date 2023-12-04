from PIL import Image
import numpy as np
import os

tickjson = "functions/tick.json"
tickjsoncommand = "functions/tick0.mcfunction"

if not os.path.exists("functions"):
    os.makedirs("functions")

if not os.path.exists(tickjson):
    with open(tickjson,"w") as file:
        file.write("{\n    \"values\": [\n        \"tick0\"\n    ]\n}") 
        
if not os.path.exists(tickjsoncommand):
    with open(tickjsoncommand,"w") as file:
        file.write("scoreboard players add @p[tag=printing] print 1\n") 

print("Type the .png name")
png_name = str(input())
print("0:Picture and Function Generation\n1:Only Function Generation\nType 0 or 1")
onlyfuncmode = int(input())
if(onlyfuncmode == 0):
    print("0:Full Block\n1:24 Block\n1:Only Wool Block\nType 0,1 or 2")
    blockmode = int(input())



folder_path = "functions/{}".format(png_name)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
image = Image.open("{}.png".format(png_name))
print("{0}x{1} pixel".format(image.width,image.height))
print("{0}x{1} block".format(1+int(image.width/64),1+int(image.height/64)))
class allblock:
    fullblocks = [
        [127,178,56,"slime"],
        [247,233,163,"sand"],
        [255,0,0,"redstone_block"],
        [160,160,255,"ice"],
        [167,167,167,"iron_block"],
        [0,124,0,"leaves"],
        [255,255,255,"white_wool"],
        [164,168,184,"clay"],
        [151,109,77,"dirt"],
        [112,112,112,"stone"],
        [143, 119, 72,"planks"],
        [255, 252, 245,"quartz_block"],
        [216, 127, 51,"orange_wool"],
        [178, 76, 216,"magenta_wool"],
        [102, 153, 216,"light_blue_wool"],
        [229, 229, 51,"yellow_wool"],
        [127, 204, 25,"lime_wool"],
        [242, 127, 165,"pink_wool"],
        [76, 76, 76,"gray_wool"],
        [153, 153, 153,"light_gray_wool"],
        [76, 127, 153,"cyan_wool"],
        [127, 63, 178,"purple_wool"],
        [51, 76, 178,"blue_wool"],
        [102, 76, 51,"brown_wool"],
        [102, 127, 51,"green_wool"],
        [153, 51, 51,"red_wool"],
        [25, 25, 25,"black_wool"],
        [250, 238, 77,"gold_block"],
        [92, 219, 213,"diamond_block"],
        [74, 128, 255,"lapis_block"],
        [0, 217, 58,"emerald_block"],
        [112, 2, 0,"red_nether_brick"],
        [209, 177, 161,"white_terracotta"],
        [159, 82, 36,"orange_terracotta"],
        [149, 87, 108,"magenta_terracotta"],
        [112, 108, 138,"light_blue_terracotta"],
        [186, 133, 36,"yellow_terracotta"],
        [103, 117, 53,"lime_terracotta"],
        [160, 77, 78,"pink_terracotta"],
        [57, 41, 35,"gray_terracotta"],
        [135, 107, 98,"light_gray_terracotta"],
        [87, 92, 92,"cyan_terracotta"],
        [122, 73, 88,"purple_terracotta"],
        [76, 62, 92,"blue_terracotta"],
        [76, 50, 35,"brown_terracotta"],
        [76, 82, 42,"green_terracotta"],
        [142, 60, 46,"red_terracotta"],
        [37, 22, 16,"black_terracotta"],
        [100, 100, 100,"deepslate"]
    ]
    blocks_24 = [
        [255,255,255,"white_wool"],
        [216, 127, 51,"orange_wool"],
        [178, 76, 216,"magenta_wool"],
        [102, 153, 216,"light_blue_wool"],
        [229, 229, 51,"yellow_wool"],
        [127, 204, 25,"lime_wool"],
        [242, 127, 165,"pink_wool"],
        [76, 76, 76,"gray_wool"],
        [153, 153, 153,"light_gray_wool"],
        [76, 127, 153,"cyan_wool"],
        [127, 63, 178,"purple_wool"],
        [51, 76, 178,"blue_wool"],
        [102, 76, 51,"brown_wool"],
        [102, 127, 51,"green_wool"],
        [153, 51, 51,"red_wool"],
        [25, 25, 25,"black_wool"],
        [247,233,163,"sand"],
        [250, 238, 77,"gold_block"],
        [143, 119, 72,"planks"],
        [160, 77, 78,"pink_terracotta"],
        [186, 133, 36,"yellow_terracotta"],
        [209, 177, 161,"white_terracotta"],
        [92, 219, 213,"diamond_block"],
        [142, 60, 46,"red_terracotta"]
    ]
    blocks_16 = [
        [255,255,255,"white_wool"],
        [216, 127, 51,"orange_wool"],
        [178, 76, 216,"magenta_wool"],
        [102, 153, 216,"light_blue_wool"],
        [229, 229, 51,"yellow_wool"],
        [127, 204, 25,"lime_wool"],
        [242, 127, 165,"pink_wool"],
        [76, 76, 76,"gray_wool"],
        [153, 153, 153,"light_gray_wool"],
        [76, 127, 153,"cyan_wool"],
        [127, 63, 178,"purple_wool"],
        [51, 76, 178,"blue_wool"],
        [102, 76, 51,"brown_wool"],
        [102, 127, 51,"green_wool"],
        [153, 51, 51,"red_wool"],
        [25, 25, 25,"black_wool"]
    ]


def printblock(image_array,x,y):
    image_block_index = [[0 for j in range(len(image_array[0]))] for i in range(len(image_array))]
    for i in range(len(image_array)):
        for j in range(len(image_array[0])):
            min_sum = 65535
            min_index = 0
            for k in range(48):
                sum = 0
                sum = sum + np.power(np.abs(image_array[i][j][0] - allblock.fullblocks[k][0]),2)
                sum = sum + np.power(np.abs(image_array[i][j][1] - allblock.fullblocks[k][1]),2)
                sum = sum + np.power(np.abs(image_array[i][j][2] - allblock.fullblocks[k][2]),2)
                if(sum < min_sum):
                    min_sum = sum
                    min_index = k
            image_block_index[i][j] = min_index
    with open("functions/{0}/x{1}y{2}.mcfunction".format(png_name,x,y),"w") as file:
        for i in range(len(image_array)):
            for j in range(len(image_array[0])):
                file.write("setblock ~{1}~~{0} {2} \n".format(i,j,allblock.fullblocks[image_block_index[i][j]][3]))   

                
def printblock24(image_array,x,y):
    image_block_index = [[0 for j in range(len(image_array[0]))] for i in range(len(image_array))]
    for i in range(len(image_array)):
        for j in range(len(image_array[0])):
            min_sum = 65535
            min_index = 0
            for k in range(23):
                sum = 0
                sum = sum + np.power(np.abs(image_array[i][j][0] - allblock.blocks_24[k][0]),2)
                sum = sum + np.power(np.abs(image_array[i][j][1] - allblock.blocks_24[k][1]),2)
                sum = sum + np.power(np.abs(image_array[i][j][2] - allblock.blocks_24[k][2]),2)
                if(sum < min_sum):
                    min_sum = sum
                    min_index = k
            image_block_index[i][j] = min_index
    with open("functions/{0}/x{1}y{2}.mcfunction".format(png_name,x,y),"w") as file:
        for i in range(len(image_array)):
            for j in range(len(image_array[0])):
                file.write("setblock ~{1}~~{0} {2} \n".format(i,j,allblock.blocks_24[image_block_index[i][j]][3]))   
                
def printblock16(image_array,x,y):
    image_block_index = [[0 for j in range(len(image_array[0]))] for i in range(len(image_array))]
    for i in range(len(image_array)):
        for j in range(len(image_array[0])):
            min_sum = 65535
            min_index = 0
            for k in range(15):
                sum = 0
                sum = sum + np.power(np.abs(image_array[i][j][0] - allblock.blocks_16[k][0]),2)
                sum = sum + np.power(np.abs(image_array[i][j][1] - allblock.blocks_16[k][1]),2)
                sum = sum + np.power(np.abs(image_array[i][j][2] - allblock.blocks_16[k][2]),2)
                if(sum < min_sum):
                    min_sum = sum
                    min_index = k
            image_block_index[i][j] = min_index
    with open("functions/{0}/x{1}y{2}.mcfunction".format(png_name,x,y),"w") as file:
        for i in range(len(image_array)):
            for j in range(len(image_array[0])):
                file.write("setblock ~{1}~~{0} {2} \n".format(i,j,allblock.blocks[image_block_index[i][j]][3]))   

x = 0
y = 0

if(onlyfuncmode == 0):
    for y in range(1+int(image.height/64)):

        if(image.height - 64 * y < 64):
            y1 = image.height
        else:
            y1 = 64 + 64 * y
        
        for x in range(1+int(image.width/64)):
            if(image.width - 64 * x < 64):
                x1 = image.width
            else:
                x1 = 64 + 64 * x
            

            crop_box = (x*64,y*64,x1,y1)
            cropped_image = image.crop(crop_box)
            image_array = np.array(cropped_image)
            if(blockmode == 0): printblock(image_array,x,y)
            if(blockmode == 1): printblock24(image_array,x,y)
            if(blockmode == 2): printblock16(image_array,x,y)



k = 0
with open("functions/print{}.mcfunction".format(png_name),"w") as file:
    file.write("scoreboard objectives add print dummy\n") 
    file.write("scoreboard players set @p[tag=!printing] print 0\n") 
    file.write("tp @p[tag=!printing] ~64~~64\n")
    file.write("tag @p[tag=!printing] add printing{}\n".format(png_name)) 
    file.write("tag @p[tag=!printing] add printing\n") 
    for y in range(1+int(image.height/128)):
        for x in range(1+int(image.width/128)):
            k = k + 2
            if(int(image.width/64) >= x*2 and int(image.height/64) >= y*2 ): file.write("execute @p[scores={{print={3}}},tag=printing] ~-64~~-64 function {0}/x{1}y{2}\n".format(png_name,x*2,y*2,k*20)) 
            if(int(image.width/64) >= x*2+1 and int(image.height/64) >= y*2 ): file.write("execute @p[scores={{print={3}}},tag=printing] ~~~-64 function {0}/x{1}y{2}\n".format(png_name,x*2+1,y*2,1+k*20)) 
            if(int(image.width/64) >= x*2 and int(image.height/64) >= y*2+1 ): file.write("execute @p[scores={{print={3}}},tag=printing] ~-64~~ function {0}/x{1}y{2}\n".format(png_name,x*2,y*2+1,2+k*20)) 
            if(int(image.width/64) >= x*2+1 and int(image.height/64) >= y*2+1 ): file.write("execute @p[scores={{print={3}}},tag=printing] ~~~ function {0}/x{1}y{2}\n".format(png_name,x*2+1,y*2+1,3+k*20)) 
            if(x != int(image.width/128)):
                file.write("tp @p[scores={{print={}}},tag=printing] ~128~~\n".format(4+k*20))
        file.write("tp @p[scores={{print={1}}},tag=printing] ~-{0}~~128\n".format((x)*128,4+k*20)) 
    k = k + 1
    file.write("tag @p[scores={{print={0}..}},tag=printing] remove printing{1}\n".format(k*20,png_name)) 
    file.write("tag @p[scores={{print={}..}},tag=printing] remove printing\n".format(k*20)) 

command = str("execute @p[tag=printing,tag=printing{0}] ~~~ function print{0}\n".format(png_name))
is_command_already = False

with open(tickjsoncommand,'r') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        if(lines[i] == command):
            is_command_already = True
    if(is_command_already == False):
        lines.insert(1,command)


if(is_command_already == False):
    with open(tickjsoncommand,'w') as file:
        file.writelines(lines)