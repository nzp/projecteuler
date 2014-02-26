; Multiples of 3 and 5
;
; If we list all the natural numbers below 10 that are multiples of 3 or 5,
; we get 3, 5, 6 and 9. The sum of these multiples is 23.
; Find the sum of all the multiples of 3 or 5 below 1000.

; I'm sure this could be made much better, but I'm practically working
; based on conceptual understanding of Lisp in general and very
; superficial knowledge of Scheme.

(use extras) ; For print to stdout in Chicken Scheme
(use srfi-1) ; For filter

(define (is-multiple? value)
  (cond ((or (= (modulo value 3) 0)
	     (= (modulo value 5) 0))
	 #t)
	(else #f)))

(define (integer-list n)
  (if (= n 0)
     '() 
      (cons n (integer-list (- n 1)))))

(define (get-multiples bound)
  (filter is-multiple? (integer-list bound)))

(define (sum-of-multiples lst)
  (foldl + 0 lst))

(format #t 
	"The sum of multiples is ~A.\n" 
	(sum-of-multiples (get-multiples 999)))
