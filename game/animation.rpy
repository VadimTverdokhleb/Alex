#init python:

    # определяем функцию для создания анимации изображения
    #def image_animation(image, animation):
        #image_show(image)  # отображаем изображение
        #for i in range(len(animation)):
            #renpy.pause(animation[i][0])  # приостанавливаем на заданный промежуток времени
            #image(image=animation[i][1])  # меняем изображение
        #renpy.pause(0.5)  # приостанавливаем на полсекунды

    # создаем анимацию для изображения, которое будет показываться через команду "call animation image"
    #image_animation('image_name.png', [(1, 'image_name.png'), (1, 'image_name_2.png'), (1, 'image_name_3.png')])
