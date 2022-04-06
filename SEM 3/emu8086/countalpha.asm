
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

include 'emu8086.inc'

org 100h

; add your code here


.data

string1 db "osg College Of TechNologyP"

.code

comp proc
     
     loop1:
        cmp string1[bx],80
        je l2
        cmp string1[bx],111
        je l1
        
        inc bx
     
        loop loop1
     l2:   
     ret

l1:
    inc ax
    inc bx
    loop loop1     

ret




