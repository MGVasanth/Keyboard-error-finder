import pygame

pygame.init()

window = pygame.display.set_mode((800,400))
background = pygame.image.load("Keyboard.jpg")
pygame.display.set_icon(background)


pygame.display.set_caption("Keyboard Error Finder")


running = True

while running:

    for event in pygame.event.get():
        
        # quit
        if event.type == pygame.QUIT:
            pygame.quit()
        # escape
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Escape")
                esc = pygame.image.load("escape.jpg")
                esc_loc = esc.get_rect()
                esc_loc.center = 400,200
                window.blit(esc,esc_loc)
            if event.key == pygame.K_a:
                print("a")
                a = pygame.image.load("a.png")
                a_loc = a.get_rect()
                a_loc.center = 400,200
                window.blit(a,a_loc)
            if event.key == pygame.K_b:
                print("b")
                b = pygame.image.load("b.jpg")
                b_loc = b.get_rect()
                b_loc.center = 400,200
                window.blit(b,b_loc)
            if event.key == pygame.K_c:
                print("c")
                c = pygame.image.load("c.jpg")
                c_loc = c.get_rect()
                c_loc.center = 400,200
                window.blit(c,c_loc)
            if event.key == pygame.K_d:
                print("d")
                d = pygame.image.load("d.jpg")
                d_loc = d.get_rect()
                d_loc.center = 400,200
                window.blit(d,d_loc)
            if event.key == pygame.K_e:
                print("e")
                e = pygame.image.load("e.jpg")
                e_loc = e.get_rect()
                e_loc.center = 400,200
                window.blit(e,e_loc)
            if event.key == pygame.K_f:
                print("f")
                f = pygame.image.load("f.jpg")
                f_loc = f.get_rect()
                f_loc.center = 400,200
                window.blit(f,f_loc)
            if event.key == pygame.K_g:
                print("g")
                g = pygame.image.load("g.jpg")
                g_loc = g.get_rect()
                g_loc.center = 400,200
                window.blit(g,g_loc)
            if event.key == pygame.K_h:
                print("h")
                h = pygame.image.load("h.jpg")
                h_loc = h.get_rect()
                h_loc.center = 400,200
                window.blit(h,h_loc)
            if event.key == pygame.K_i:
                print("i")
                i = pygame.image.load("i.png")
                i_loc = i.get_rect()
                i_loc.center = 400,200
                window.blit(i,i_loc)
            if event.key == pygame.K_j:
                print("j")
                j = pygame.image.load("j.jpg")
                j_loc = j.get_rect()
                j_loc.center = 400,200
                window.blit(j,j_loc)
            if event.key == pygame.K_k:
                print("k")
                k = pygame.image.load("k.jpg")
                k_loc = k.get_rect()
                k_loc.center = 400,200
                window.blit(k,k_loc)
            if event.key == pygame.K_l:
                print("l")
                l = pygame.image.load("l.jpg")
                l_loc = a.get_rect()
                l_loc.center = 400,200
                window.blit(l,l_loc)
            if event.key == pygame.K_m:
                print("m")
                m = pygame.image.load("m.jpg")
                m_loc = m.get_rect()
                m_loc.center = 400,200
                window.blit(m,m_loc)
            if event.key == pygame.K_n:
                print("n")
                n = pygame.image.load("n.jpg")
                n_loc = n.get_rect()
                n_loc.center = 400,200
                window.blit(n,n_loc)
            if event.key == pygame.K_o:
                print("o")
                o = pygame.image.load("o.jpg")
                o_loc = o.get_rect()
                o_loc.center = 400,200
                window.blit(o,o_loc)
            if event.key == pygame.K_p:
                print("p")
                p = pygame.image.load("p.jpg")
                p_loc = p.get_rect()
                p_loc.center = 400,200
                window.blit(p,p_loc)
            if event.key == pygame.K_q:
                print("q")
                q = pygame.image.load("q.jpg")
                q_loc = q.get_rect()
                q_loc.center = 400,200
                window.blit(q,q_loc)
            if event.key == pygame.K_r:
                print("r")
                r = pygame.image.load("r.jpg")
                r_loc = r.get_rect()
                r_loc.center = 400,200
                window.blit(r,r_loc)
            if event.key == pygame.K_s:
                print("s")
                s = pygame.image.load("s.jpg")
                s_loc = s.get_rect()
                s_loc.center = 400,200
                window.blit(s,s_loc)
            if event.key == pygame.K_t:
                print("t")
                t = pygame.image.load("t.jpg")
                t_loc = t.get_rect()
                t_loc.center = 400,200
                window.blit(t,t_loc)
            if event.key == pygame.K_u:
                print("u")
                u = pygame.image.load("u.jpg")
                u_loc = u.get_rect()
                u_loc.center = 400,200
                window.blit(u,u_loc)
            if event.key == pygame.K_v:
                print("v")
                v = pygame.image.load("v.jpg")
                v_loc = v.get_rect()
                v_loc.center = 400,200
                window.blit(v,v_loc)
            if event.key == pygame.K_w:
                print("w")
                w = pygame.image.load("w.jpg")
                w_loc = w.get_rect()
                w_loc.center = 400,200
                window.blit(w,w_loc)
            if event.key == pygame.K_x:
                print("x")
                x = pygame.image.load("x.jpg")
                x_loc = x.get_rect()
                x_loc.center = 400,200
                window.blit(x,x_loc)
            if event.key == pygame.K_y:
                print("y")
                y = pygame.image.load("y.jpg")
                y_loc = y.get_rect()
                y_loc.center = 400,200
                window.blit(y,y_loc)
            if event.key == pygame.K_z:
                print("z")
                z = pygame.image.load("z.jpg")
                z_loc = z.get_rect()
                z_loc.center = 400,200
                window.blit(z,z_loc)
            if event.key == pygame.K_0:
                print("zero")
                zero = pygame.image.load("0.png")
                zero_loc = zero.get_rect()
                zero_loc.center = 400,200
                window.blit(zero,zero_loc)
            if event.key == pygame.K_1:
                print("one")
                one = pygame.image.load("one.png")
                one_loc = one.get_rect()
                one_loc.center = 400,200
                window.blit(one,one_loc)
            if event.key == pygame.K_2:
                print("two")
                two = pygame.image.load("2.jpg")
                two_loc = two.get_rect()
                two_loc.center = 400,200
                window.blit(two,two_loc)
            if event.key == pygame.K_3:
                print("three")
                three = pygame.image.load("3.png")
                three_loc = three.get_rect()
                three_loc.center = 400,200
                window.blit(three,three_loc)
            if event.key == pygame.K_4:
                print("four")
                four = pygame.image.load("4.png")
                four_loc = four.get_rect()
                four_loc.center = 400,200
                window.blit(four,four_loc)
            if event.key == pygame.K_5:
                print("five")
                five = pygame.image.load("5.png")
                five_loc = five.get_rect()
                five_loc.center = 400,200
                window.blit(five,five_loc)
            if event.key == pygame.K_6:
                print("six")
                six = pygame.image.load("6.png")
                six_loc = six.get_rect()
                six_loc.center = 400,200
                window.blit(six,six_loc)
            if event.key == pygame.K_7:
                print("seven")
                seven = pygame.image.load("7.png")
                seven_loc = seven.get_rect()
                seven_loc.center = 400,200
                window.blit(seven,seven_loc)
            if event.key == pygame.K_8:
                print("eight")
                eight = pygame.image.load("8.png")
                eight_loc = eight.get_rect()
                eight_loc.center = 400,200
                window.blit(eight,eight_loc)
            if event.key == pygame.K_9:
                print("9")
                nine = pygame.image.load("9.png")
                nine_loc = nine.get_rect()
                nine_loc.center = 400,200
                window.blit(nine,nine_loc)
            if event.key == pygame.K_INSERT:
                print("INSERT")
                insert = pygame.image.load("insert.png")
                insert_loc = insert.get_rect()
                insert_loc.center = 400,200
                window.blit(insert,insert_loc)
            if event.key == pygame.K_HOME:
                print("home")
                home = pygame.image.load("home.jpg")
                home_loc = home.get_rect()
                home_loc.center = 400,200
                window.blit(home,home_loc)
            if event.key == pygame.K_PAGEUP:
                print("Pageup")
                pageup = pygame.image.load("pageup.png")
                pageup_loc = pageup.get_rect()
                pageup_loc.center = 400,200
                window.blit(pageup,pageup_loc)
            if event.key == pygame.K_DELETE:
                print("delete")
                delete = pygame.image.load("delete.jpg")
                delete_loc = delete.get_rect()
                delete_loc.center = 400,200
                window.blit(delete,delete_loc)
            if event.key == pygame.K_END:
                print("end")
                end = pygame.image.load("end.jpg")
                end_loc = end.get_rect()
                end_loc.center = 400,200
                window.blit(end,end_loc)
            if event.key == pygame.K_PAGEDOWN:
                print("pagedown")
                pagedown = pygame.image.load("pagedown.png")
                pagedown_loc = pagedown.get_rect()
                pagedown_loc.center = 400,200
                window.blit(pagedown,pagedown_loc)
            if event.key == pygame.K_KP_DIVIDE:
                print("/")
                slash = pygame.image.load("slash.jpg")
                slash_loc = slash.get_rect()
                slash_loc.center = 400,200
                window.blit(slash,slash_loc)
            if event.key == pygame.K_KP_MULTIPLY:
                print("*")
                asterisk = pygame.image.load("asterisk.png")
                asterisk_loc = asterisk.get_rect()
                asterisk_loc.center = 400,200
                window.blit(asterisk,asterisk_loc)
            if event.key == pygame.K_KP_MINUS:
                print("-")
                minus = pygame.image.load("minus.png")
                minus_loc = minus.get_rect()
                minus_loc.center = 400,200
                window.blit(minus,minus_loc)
            if event.key == pygame.K_KP_PLUS:
                print("+")
                plus = pygame.image.load("plus.png")
                plus_loc = plus.get_rect()
                plus_loc.center = 400,200
                window.blit(plus,plus_loc)
            if event.key == pygame.K_KP_ENTER or event.key == pygame.KSCAN_KP_ENTER:
                print("enter")
                enter = pygame.image.load("enter.png")
                enter_loc = enter.get_rect()
                enter_loc.center = 400,200
                window.blit(enter,enter_loc)
            if event.key == pygame.K_UP:
                print("up arrow")
                arr1 = pygame.image.load("arrup.png")
                arr1_loc = arr1.get_rect()
                arr1_loc.center = 400,200
                window.blit(arr1,arr1_loc)
            if event.key == pygame.K_DOWN:
                print("down")
                arr2 = pygame.image.load("arrdown.png")
                arr2_loc = arr2.get_rect()
                arr2_loc.center = 400,200
                window.blit(arr2,arr2_loc)
            if event.key == pygame.K_RIGHT:
                print("Right")
                arr3 = pygame.image.load("arrright.png")
                arr3_loc = arr3.get_rect()
                arr3_loc.center = 400,200
                window.blit(arr3,arr3_loc)
            if event.key == pygame.K_LEFT:
                print("Left")
                arr4 = pygame.image.load("arrleft.png")
                arr4_loc = arr4.get_rect()
                arr4_loc.center = 400,200
                window.blit(arr4,arr4_loc)



        pygame.display.update()




