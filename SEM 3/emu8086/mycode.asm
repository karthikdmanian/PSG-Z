
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

; add your code here

mov ax,10h;
mov bx,7h;

;call swap 

call comp

;swap proc
    
    ;mov cx,ax;
    
    ;mov ax,bx;
    
    ;mov bx,cx;

;swap endp

comp proc
    
    cmp bx,ax;
    
    jmp l1;
    
    l1: mov ax,bx;
        
comp endp

ret




