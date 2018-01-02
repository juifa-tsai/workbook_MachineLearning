#!/bin/tcsh
if ( $3 == "" ) then
    echo "[NOTE] ./reWord.csh [path] [text1] [text2]"
    echo "       Change [text1] to [text2] for files under [path]"
    exit
endif

echo "[WARNING] change text $2 -> $3 under $1 (y/n)?"
set y = 0
while ( $y != 1 )
    set option = $<
    if ( $option == 'y' || $option == 'Y' ) then
        set y=1
    else if ( $option == 'n' || $option == 'N' ) then
        exit
    else
        echo "[WARNING] change text $2 -> $3 under $1 (y/n)?"
    endif 
end 

set tracing = 1
set n_changed = 0
while ( $tracing )
    set f=`grep -r --exclude-dir='./*/.*' -m 1 "$2" $1 | awk -F ":" '{print $1}'`
    if ( $f == "" ) then
        set tracing = 0
    else
        set text1 = `echo $2 | sed 's/\./\\./g' | sed 's/\//\\\//g'`
        set text2 = `echo $3 | sed 's/\./\\./g' | sed 's/\//\\\//g'`
        sed -i '' "s/$text1/$text2/g" $f
        echo $f' .... -> changed'
        @ n_changed++
    endif
end
echo "[DONE] $n_changed changed : $2 -> $3 "
