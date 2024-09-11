(define (filter-lst fn lst)
  (if (equal? nil lst)
    nil
    (if (fn (car lst))
      (cons (car lst) (filter-lst fn (cdr lst)))
      (filter-lst fn (cdr lst))
      )
    )
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)


(define (interleave first second)
  (if (null? first)
    second
    (if (null? second)
      first
      (append (list (car first) (car second)) (interleave (cdr first) (cdr second)))
      )
    )
)

(interleave (list 1 3 5) (list 2 4 6))
; expect (1 2 3 4 5 6)

(interleave (list 1 3 5) nil)
; expect (1 3 5)

(interleave (list 1 3 5) (list 2 4))
; expect (1 2 3 4 5)


(define (accumulate combiner start n term)
  (if (= 0 n)
    start
    (accumulate combiner (combiner start (term n)) (- n 1) term)
    )
)


(define (no-repeats lst)
  (if (null? lst)
    nil
    (begin
      (define neq (lambda (x y) (not (= x y ))))
      (define (neq_x x) 
        (lambda (num) (neq num x))
      )
      (define newlst (filter-lst (neq_x (car lst)) lst))
      (cons (car lst) (no-repeats newlst))
      )
    )
)

