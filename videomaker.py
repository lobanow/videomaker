# -*- coding: utf-8 -*-


from moviepy.editor import VideoFileClip, vfx, ImageClip, AudioFileClip, concatenate_videoclips
import os

def videomaker():
            audioclip = AudioFileClip("../my_result.mp3")

            image_folder=os.getcwd()
            print(image_folder)
            first_frame = 1
            count=0
            for img in os.listdir(image_folder):
                    if img.endswith(".jpg"):
                        print(img)
                        if first_frame == 1:
                            clip = ImageClip(img).set_duration(0)
                            first_frame=0
                        current_clip= ImageClip(img).set_duration(4).fadein(0.25).fadeout(0.25)
                        if img =='1.jpg':
                            clip = concatenate_videoclips([current_clip,clip])
                        else: 
                            clip = concatenate_videoclips([clip, current_clip])
                        count+=1

            current_audioclip=audioclip.set_duration(count*4)
            clip=clip.set_audio(current_audioclip)
            clip.write_videofile(image_folder+'.mp4',fps=30)



            
            os.chdir('..')


            clip.close
            audioclip.close        
            current_audioclip.close
            current_clip.close

def main():
        for dir in os.listdir():
            if dir=='H:\System Volume Information':
                continue
            try:
                os.chdir(dir)
                videomaker()
            except NotADirectoryError:
                pass

if __name__=="__main__":
    main()