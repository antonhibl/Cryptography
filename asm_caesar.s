	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 10, 15	sdk_version 10, 15, 6
	.globl	_main                   ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$48, %rsp
	movl	$0, -4(%rbp)
	movl	%edi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movq	-16(%rbp), %rax
	movq	8(%rax), %rax
	movq	%rax, -40(%rbp)
	cmpq	$0, %rax
	je	LBB0_24
## %bb.1:
	movq	-40(%rbp), %rax
	movsbl	(%rax), %ecx
	cmpl	$0, %ecx
	je	LBB0_24
## %bb.2:
	movq	-16(%rbp), %rax
	movq	16(%rax), %rdi
	leaq	L_.str(%rip), %rsi
	callq	_fopen
	movq	%rax, -24(%rbp)
	cmpq	$0, %rax
	je	LBB0_23
## %bb.3:
	movq	-16(%rbp), %rax
	movq	24(%rax), %rdi
	leaq	L_.str.1(%rip), %rsi
	callq	_fopen
	movq	%rax, -32(%rbp)
	cmpq	$0, %rax
	je	LBB0_22
## %bb.4:
	jmp	LBB0_5
LBB0_5:                                 ## =>This Inner Loop Header: Depth=1
	movq	-24(%rbp), %rdi
	callq	_getc
                                        ## kill: def $al killed $al killed $eax
	movb	%al, -41(%rbp)
	movsbl	%al, %ecx
	cmpl	$-1, %ecx
	je	LBB0_21
## %bb.6:                               ##   in Loop: Header=BB0_5 Depth=1
	movq	-40(%rbp), %rdi
	callq	_atoi
	movl	%eax, -48(%rbp)
	movsbl	-41(%rbp), %eax
	cmpl	$97, %eax
	jl	LBB0_11
## %bb.7:                               ##   in Loop: Header=BB0_5 Depth=1
	movsbl	-41(%rbp), %eax
	cmpl	$122, %eax
	jg	LBB0_11
## %bb.8:                               ##   in Loop: Header=BB0_5 Depth=1
	movsbl	-41(%rbp), %eax
	addl	-48(%rbp), %eax
                                        ## kill: def $al killed $al killed $eax
	movb	%al, -41(%rbp)
	movsbl	-41(%rbp), %ecx
	cmpl	$122, %ecx
	jle	LBB0_10
## %bb.9:                               ##   in Loop: Header=BB0_5 Depth=1
	movsbl	-41(%rbp), %eax
	subl	$122, %eax
	addl	$97, %eax
	subl	$1, %eax
                                        ## kill: def $al killed $al killed $eax
	movb	%al, -41(%rbp)
LBB0_10:                                ##   in Loop: Header=BB0_5 Depth=1
	movsbl	-41(%rbp), %edi
	movq	-32(%rbp), %rsi
	callq	_putc
LBB0_11:                                ##   in Loop: Header=BB0_5 Depth=1
	movsbl	-41(%rbp), %eax
	cmpl	$65, %eax
	jl	LBB0_16
## %bb.12:                              ##   in Loop: Header=BB0_5 Depth=1
	movsbl	-41(%rbp), %eax
	cmpl	$90, %eax
	jg	LBB0_16
## %bb.13:                              ##   in Loop: Header=BB0_5 Depth=1
	movsbl	-41(%rbp), %eax
	addl	-48(%rbp), %eax
                                        ## kill: def $al killed $al killed $eax
	movb	%al, -41(%rbp)
	movsbl	-41(%rbp), %ecx
	cmpl	$90, %ecx
	jle	LBB0_15
## %bb.14:                              ##   in Loop: Header=BB0_5 Depth=1
	movsbl	-41(%rbp), %eax
	subl	$90, %eax
	addl	$65, %eax
	subl	$1, %eax
                                        ## kill: def $al killed $al killed $eax
	movb	%al, -41(%rbp)
LBB0_15:                                ##   in Loop: Header=BB0_5 Depth=1
	movsbl	-41(%rbp), %edi
	movq	-32(%rbp), %rsi
	callq	_putc
	jmp	LBB0_20
LBB0_16:                                ##   in Loop: Header=BB0_5 Depth=1
	movsbl	-41(%rbp), %eax
	cmpl	$32, %eax
	jne	LBB0_18
## %bb.17:                              ##   in Loop: Header=BB0_5 Depth=1
	movb	$32, -41(%rbp)
	jmp	LBB0_19
LBB0_18:                                ##   in Loop: Header=BB0_5 Depth=1
	movsbl	-41(%rbp), %eax
	addl	-48(%rbp), %eax
                                        ## kill: def $al killed $al killed $eax
	movb	%al, -41(%rbp)
LBB0_19:                                ##   in Loop: Header=BB0_5 Depth=1
	movsbl	-41(%rbp), %edi
	movq	-32(%rbp), %rsi
	callq	_putc
LBB0_20:                                ##   in Loop: Header=BB0_5 Depth=1
	jmp	LBB0_5
LBB0_21:
	jmp	LBB0_22
LBB0_22:
	movq	-32(%rbp), %rdi
	callq	_fclose
LBB0_23:
	movq	-24(%rbp), %rdi
	callq	_fclose
LBB0_24:
	xorl	%eax, %eax
	addq	$48, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"rb"

L_.str.1:                               ## @.str.1
	.asciz	"wb"

.subsections_via_symbols
