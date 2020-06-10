import image_process_function

v='水滴.mp4'
i='patrick.jpg'

frames=[]
# frames,fps=image_process_function.get_video(v)
frames=image_process_function.get_image(i)
#frames=image_process_function.color(frames,0.114,0.587,0.229)
#frames=image_process_function.size(frames,50,50)
#frames=image_process_function.gray(frames)
# image_process_function.write_video('test.mp4',frames,fps)
#image_process_function.write_image('test.jpg',frames)
frames=image_process_function.edgeEnhance(frames)
image_process_function.write_image('edgeEn.jpg',frames)
