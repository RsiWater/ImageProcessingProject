import image_process_f

v='水滴.mp4'
video_size=image_process_f.size_f(v,100,100)
video_gray=image_process_f.gray(v)
image_process_f.write_video('size.mp4',video_size[0],video_size[1],video_size[2])
image_process_f.write_video('gray.mp4',video_gray[0],video_gray[1],video_gray[2])