(use-modules
 (ice-9 popen)
 (ice-9 match)
 (ice-9 rdelim)
 (guix packages)
 (guix build-system python)
 (guix gexp)
 ((guix build utils) #:select (with-directory-excursion))
 (gnu packages)
 (gnu packages python)
 (gnu packages glib)
 (gnu packages gtk)
 ((guix licenses) #:prefix license:))

(define %source-dir (dirname (current-filename)))

(define-public cia-git
  (package
    (name "cia-git")
    (version (string-append "0.0" "-dev"))    
    (source
     (local-file %source-dir
                 #:recursive? #t))
    (build-system python-build-system)
    (inputs
     `(("python-colorama" ,python-colorama)))
    (home-page "https://n0.is/s/cia")
    (synopsis "")
    (description "")
    (license #f)))

cia-git
