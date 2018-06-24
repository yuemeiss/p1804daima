def key_control(enemy,hero,move_step):
    '''游戏事件的监听'''
    keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        for i in hero.bullet_list:
            if pygame.Rect.colliderect(i.b_rect,enemy.rect):
                enemy.baozha()
                del enemy
                break
        if event.type == pygame.QUIT:  #退出游戏
            print('退出游戏')
            pygame.quit()
            exit()  #退出程序
        elif keys_pressed[pygame.K_SPACE]:
            hero.fire()
        elif keys_pressed[pygame.K_b]:
            hero.baozha()
            enemy.baozha()
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        hero.rect.y -= move_step
        if hero.rect.y <= 0:
            hero.rect.y = 0
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        hero.rect.y += move_step
        if hero.rect.y >= 728:
            hero.rect.y = 728
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        hero.rect.x -= move_step
        if hero.rect.x <= -40:
            hero.rect.x = -40
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        hero.rect.x += move_step
        if hero.rect.x >=420:
            hero.rect.x = 420
