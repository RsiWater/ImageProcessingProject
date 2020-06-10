import image_process_function

v='水滴.mp4'
i='patrick.jpg'

frames=[]

frames,fps=image_process_function.get_video(v)
dframes, dfps=image_process_function.fpsDrop(frames,fps)
dframes=image_process_function.edgeEnMore(dframes)
image_process_function.write_video('water.mp4',dframes,dfps)

'''frames=image_process_function.get_image(i)
frames=image_process_function.findEdge(frames)
image_process_function.write_image('findE.jpg',frames)

frames=image_process_function.get_image(i)
frames=image_process_function.edgeEnhance(frames)
image_process_function.write_image('edgeEn.jpg',frames)

frames=image_process_function.get_image(i)
frames=image_process_function.edgeEnMore(frames)
image_process_function.write_image('edgeEnMore.jpg',frames)

frames=image_process_function.get_image(i)
frames=image_process_function.emboss(frames)
image_process_function.write_image('emboss.jpg',frames)'''