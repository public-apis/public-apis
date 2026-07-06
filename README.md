# glibc — 公共 API 索引

> 以 **glibc (GNU C Library)** 为根本的公共 API 索引。本仓库手工维护，按照功能模块分类，列出 C 库提供的核心函数、头文件与线程安全属性，供系统编程时快速查阅。

> 本项目以 [public-apis](https://github.com/public-apis/public-apis) 项目的文档格式规范为参考。所有 API 条目统一以 **5 列表格**呈现：**Function | Header | Description | Standard | MT-Safe**。

> 🔍 在线可搜索界面：https://ghshhf.github.io/public-apis/ （由 `site/` 静态站点提供，零后端、纯前端过滤）

<br >

---

## Index

* [Standard I/O (stdio.h)](#standard-io-stdioh)
* [Character & String (string.h, ctype.h)](#character--string-stringh-ctypeh)
* [Memory Management (stdlib.h, sys/mman.h)](#memory-management-stdlibh-sysmmanh)
* [Math Library (math.h)](#math-library-mathh)
* [Time & Date (time.h, sys/time.h)](#time--date-timeh-systimeh)
* [File System (unistd.h, sys/stat.h, fcntl.h, dirent.h)](#file-system-unistdh-sysstath-fcntlh-direnth)
* [Process Control (unistd.h, sys/wait.h)](#process-control-unistdh-syswaith)
* [Signal Handling (signal.h)](#signal-handling-signalh)
* [Environment & System Info (unistd.h, sys/utsname.h)](#environment--system-info-unistdh-sysutsnameh)
* [Error Handling (errno.h)](#error-handling-errnoh)
* [Locale & Internationalization (locale.h, libintl.h, iconv.h)](#locale--internationalization-localeh-libintlh-iconvh)
* [Regular Expressions (regex.h)](#regular-expressions-regexh)
* [Dynamic Linking (dlfcn.h)](#dynamic-linking-dlfcnh)
* [Threading (pthread.h)](#threading-pthreadh)
* [Synchronization Primitives](#synchronization-primitives)
* [Networking & Sockets (sys/socket.h, netinet/in.h, arpa/inet.h, netdb.h)](#networking--sockets-syssocketh-netinetinh-arpaineth-netdbh)
* [Wide Character & Multibyte (wchar.h, wctype.h)](#wide-character--multibyte-wcharh-wctypeh)
* [Complex Math (complex.h)](#complex-math-complexh)
* [Searching & Sorting (stdlib.h, search.h)](#searching--sorting-stdlibh-searchh)
* [Random Numbers (stdlib.h)](#random-numbers-stdlibh)

<br >

---

## Standard I/O (stdio.h)

### Stream Open/Close

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [fopen](https://man7.org/linux/man-pages/man3/fopen.3.html) | `<stdio.h>` | Open a file and associate a stream with it | POSIX.1-2001, C89 | Yes |
| [freopen](https://man7.org/linux/man-pages/man3/freopen.3.html) | `<stdio.h>` | Open the file whose name is the string pointed to by pathname and associates the stream pointed to by stream with it | POSIX.1-2001, C89 | Yes |
| [fdopen](https://man7.org/linux/man-pages/man3/fdopen.3.html) | `<stdio.h>` | Associate a stream with an existing file descriptor | POSIX.1-2001, POSIX.1-2008 | Yes |
| [fclose](https://man7.org/linux/man-pages/man3/fclose.3.html) | `<stdio.h>` | Flush and close a stream | POSIX.1-2001, C89 | Yes |
| [fileno](https://man7.org/linux/man-pages/man3/fileno.3.html) | `<stdio.h>` | Examine the argument stream and return its integer file descriptor | POSIX.1-2001, POSIX.1-2008 | Yes |

### Formatted I/O

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [printf](https://man7.org/linux/man-pages/man3/printf.3.html) | `<stdio.h>` | Write formatted output to stdout | POSIX.1-2001, C89 | Yes |
| [fprintf](https://man7.org/linux/man-pages/man3/fprintf.3.html) | `<stdio.h>` | Write formatted output to the given stream | POSIX.1-2001, C89 | Yes |
| [sprintf](https://man7.org/linux/man-pages/man3/sprintf.3.html) | `<stdio.h>` | Write formatted output to a character array | POSIX.1-2001, C89 | Yes |
| [snprintf](https://man7.org/linux/man-pages/man3/snprintf.3.html) | `<stdio.h>` | Write formatted output to a character array with size limit | POSIX.1-2001, C99 | Yes |
| [scanf](https://man7.org/linux/man-pages/man3/scanf.3.html) | `<stdio.h>` | Read formatted input from stdin | POSIX.1-2001, C89 | Yes |
| [fscanf](https://man7.org/linux/man-pages/man3/fscanf.3.html) | `<stdio.h>` | Read formatted input from the given stream | POSIX.1-2001, C89 | Yes |
| [sscanf](https://man7.org/linux/man-pages/man3/sscanf.3.html) | `<stdio.h>` | Read formatted input from a character array | POSIX.1-2001, C89 | Yes |
| [vprintf](https://man7.org/linux/man-pages/man3/vprintf.3.html) | `<stdio.h>` | Equivalent to printf with variable argument list | POSIX.1-2001, C89 | Yes |
| [vfprintf](https://man7.org/linux/man-pages/man3/vfprintf.3.html) | `<stdio.h>` | Equivalent to fprintf with variable argument list | POSIX.1-2001, C89 | Yes |
| [vsprintf](https://man7.org/linux/man-pages/man3/vsprintf.3.html) | `<stdio.h>` | Equivalent to sprintf with variable argument list | POSIX.1-2001, C89 | Yes |
| [vsnprintf](https://man7.org/linux/man-pages/man3/vsnprintf.3.html) | `<stdio.h>` | Equivalent to snprintf with variable argument list | POSIX.1-2001, C99 | Yes |
| [perror](https://man7.org/linux/man-pages/man3/perror.3.html) | `<stdio.h>` | Print a message describing the error code in errno | POSIX.1-2001, C89 | Yes |

### Character & String I/O

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [fgetc](https://man7.org/linux/man-pages/man3/fgetc.3.html) | `<stdio.h>` | Read the next character from stream and return it as unsigned char cast to int | POSIX.1-2001, C89 | Yes |
| [getc](https://man7.org/linux/man-pages/man3/getc.3.html) | `<stdio.h>` | Equivalent to fgetc except that it may be implemented as a macro | POSIX.1-2001, C89 | Yes |
| [getchar](https://man7.org/linux/man-pages/man3/getchar.3.html) | `<stdio.h>` | Equivalent to getc(stdin) | POSIX.1-2001, C89 | Yes |
| [ungetc](https://man7.org/linux/man-pages/man3/ungetc.3.html) | `<stdio.h>` | Push c back to stream, cast to unsigned char, where it is available for subsequent read operations | POSIX.1-2001, C89 | Yes |
| [fputc](https://man7.org/linux/man-pages/man3/fputc.3.html) | `<stdio.h>` | Write the character c, cast to unsigned char, to stream | POSIX.1-2001, C89 | Yes |
| [putc](https://man7.org/linux/man-pages/man3/putc.3.html) | `<stdio.h>` | Equivalent to fputc except that it may be implemented as a macro | POSIX.1-2001, C89 | Yes |
| [putchar](https://man7.org/linux/man-pages/man3/putchar.3.html) | `<stdio.h>` | Equivalent to putc(c, stdout) | POSIX.1-2001, C89 | Yes |
| [fgets](https://man7.org/linux/man-pages/man3/fgets.3.html) | `<stdio.h>` | Read in at most one less than size characters from stream | POSIX.1-2001, C89 | Yes |
| [fputs](https://man7.org/linux/man-pages/man3/fputs.3.html) | `<stdio.h>` | Write the string s to stream, without its terminating null byte | POSIX.1-2001, C89 | Yes |
| [gets](https://man7.org/linux/man-pages/man3/gets.3.html) | `<stdio.h>` | Read a line from stdin into the buffer pointed to by s until either a terminating newline or EOF, which it replaces with a null byte | POSIX.1-2001 (removed in C11) | Yes |

### Binary I/O

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [fread](https://man7.org/linux/man-pages/man3/fread.3.html) | `<stdio.h>` | Read nmemb items of data, each size bytes long, from the stream pointed to by stream | POSIX.1-2001, C89 | Yes |
| [fwrite](https://man7.org/linux/man-pages/man3/fwrite.3.html) | `<stdio.h>` | Write nmemb items of data, each size bytes long, to the stream pointed to by stream | POSIX.1-2001, C89 | Yes |

### File Positioning

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [fseek](https://man7.org/linux/man-pages/man3/fseek.3.html) | `<stdio.h>` | Set the file position indicator for the stream pointed to by stream | POSIX.1-2001, C89 | Yes |
| [ftell](https://man7.org/linux/man-pages/man3/ftell.3.html) | `<stdio.h>` | Obtain the current value of the file position indicator for the stream | POSIX.1-2001, C89 | Yes |
| [fsetpos](https://man7.org/linux/man-pages/man3/fsetpos.3.html) | `<stdio.h>` | Set the file position indicator for the stream to value of fpos_t | POSIX.1-2001, C89 | Yes |
| [fgetpos](https://man7.org/linux/man-pages/man3/fgetpos.3.html) | `<stdio.h>` | Store the current value of the file position indicator | POSIX.1-2001, C89 | Yes |
| [rewind](https://man7.org/linux/man-pages/man3/rewind.3.html) | `<stdio.h>` | Move the file position to the beginning of the file | POSIX.1-2001, C89 | Yes |

### Stream Buffering

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [fflush](https://man7.org/linux/man-pages/man3/fflush.3.html) | `<stdio.h>` | Flush a stream; if NULL make sure all pending writes complete | POSIX.1-2001, C89 | Yes |
| [setvbuf](https://man7.org/linux/man-pages/man3/setvbuf.3.html) | `<stdio.h>` | Set the buffering mode and optionally the buffer size for a stream | POSIX.1-2001, C89 | Yes |
| [setbuf](https://man7.org/linux/man-pages/man3/setbuf.3.html) | `<stdio.h>` | Set the buffer to be used for I/O operations on the stream | POSIX.1-2001, C89 | Yes |
| [setbuffer](https://man7.org/linux/man-pages/man3/setbuffer.3.html) | `<stdio.h>` | Set the buffer to be used for a stream (BSD) | BSD, SVID | Yes |
| [setlinebuf](https://man7.org/linux/man-pages/man3/setlinebuf.3.html) | `<stdio.h>` | Set line buffering for stream | 4.2BSD, SVID | Yes |

### File Operations

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [remove](https://man7.org/linux/man-pages/man3/remove.3.html) | `<stdio.h>` | Delete a name and possibly the file it refers to | POSIX.1-2001, C89 | Yes |
| [rename](https://man7.org/linux/man-pages/man3/rename.2.html) | `<stdio.h>` | Change the name or location of a file | POSIX.1-2001, C89 | Yes |
| [tmpfile](https://man7.org/linux/man-pages/man3/tmpfile.3.html) | `<stdio.h>` | Create a temporary file in binary read/write (w+b) mode | POSIX.1-2001, C89 | Yes |
| [tmpnam](https://man7.org/linux/man-pages/man3/tmpnam.3.html) | `<stdio.h>` | Return a pointer to a string that is a valid filename | POSIX.1-2001, C89 | No (race:tmpnam) |
| [tempnam](https://man7.org/linux/man-pages/man3/tempnam.3.html) | `<stdio.h>` | Return a pointer to a string that is a valid filename, in directory dir if non-NULL | POSIX.1-2001 | Yes |
| [mkstemp](https://man7.org/linux/man-pages/man3/mkstemp.3.html) | `<stdlib.h>` | Create a unique temporary file from template | POSIX.1-2001, 4.3BSD | Yes |
| [mkdtemp](https://man7.org/linux/man-pages/man3/mkdtemp.3.html) | `<stdlib.h>` | Create a unique temporary directory from template | POSIX.1-2008 | Yes |

### File Descriptor I/O (unistd.h, fcntl.h)

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [open](https://man7.org/linux/man-pages/man2/open.2.html) | `<fcntl.h>` | Open and possibly create a file | POSIX.1-2001 | Yes |
| [openat](https://man7.org/linux/man-pages/man2/openat.2.html) | `<fcntl.h>` | Equivalent to open except when pathname is relative, resolves it relative to directory referred to by dirfd | POSIX.1-2008 | Yes |
| [creat](https://man7.org/linux/man-pages/man2/creat.2.html) | `<fcntl.h>` | Create a new file or rewrite an existing one | POSIX.1-2001 | Yes |
| [close](https://man7.org/linux/man-pages/man2/close.2.html) | `<unistd.h>` | Close a file descriptor | POSIX.1-2001 | Yes |
| [read](https://man7.org/linux/man-pages/man2/read.2.html) | `<unistd.h>` | Read up to count bytes from file descriptor fd into buf | POSIX.1-2001 | Yes |
| [write](https://man7.org/linux/man-pages/man2/write.2.html) | `<unistd.h>` | Write up to count bytes from buffer buf to file descriptor fd | POSIX.1-2001 | Yes |
| [pread](https://man7.org/linux/man-pages/man2/pread.2.html) | `<unistd.h>` | Read from a file descriptor at an offset without changing the file offset | POSIX.1-2001 | Yes |
| [pwrite](https://man7.org/linux/man-pages/man2/pwrite.2.html) | `<unistd.h>` | Write to a file descriptor at an offset without changing the file offset | POSIX.1-2001 | Yes |
| [readv](https://man7.org/linux/man-pages/man2/readv.2.html) | `<sys/uio.h>` | Read data into multiple buffers | POSIX.1-2001 | Yes |
| [writev](https://man7.org/linux/man-pages/man2/writev.2.html) | `<sys/uio.h>` | Write data from multiple buffers | POSIX.1-2001 | Yes |
| [preadv](https://man7.org/linux/man-pages/man2/preadv.2.html) | `<sys/uio.h>` | Read from a file descriptor into multiple buffers at a given offset | POSIX.1-2008, Linux | Yes |
| [pwritev](https://man7.org/linux/man-pages/man2/pwritev.2.html) | `<sys/uio.h>` | Write to a file descriptor from multiple buffers at a given offset | POSIX.1-2008, Linux | Yes |
| [lseek](https://man7.org/linux/man-pages/man2/lseek.2.html) | `<unistd.h>` | Reposition read/write file offset | POSIX.1-2001 | Yes |
| [dup](https://man7.org/linux/man-pages/man2/dup.2.html) | `<unistd.h>` | Allocate a new file descriptor that refers to the same open file description | POSIX.1-2001 | Yes |
| [dup2](https://man7.org/linux/man-pages/man2/dup2.2.html) | `<unistd.h>` | Same as dup, the new file descriptor uses the specified number | POSIX.1-2001 | Yes |
| [dup3](https://man7.org/linux/man-pages/man2/dup3.2.html) | `<unistd.h>` | Same as dup2, but with additional flags | Linux | Yes |
| [fcntl](https://man7.org/linux/man-pages/man2/fcntl.2.html) | `<fcntl.h>` | Manipulate file descriptor | POSIX.1-2001 | Yes |
| [ioctl](https://man7.org/linux/man-pages/man2/ioctl.2.html) | `<sys/ioctl.h>` | Device control operations | POSIX.1-2001 | Yes |
| [pipe](https://man7.org/linux/man-pages/man2/pipe.2.html) | `<unistd.h>` | Create pipe | POSIX.1-2001 | Yes |
| [pipe2](https://man7.org/linux/man-pages/man2/pipe2.2.html) | `<fcntl.h>` | Create pipe with flags | Linux | Yes |

### Error/Status

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [feof](https://man7.org/linux/man-pages/man3/feof.3.html) | `<stdio.h>` | Test the end-of-file indicator for the stream | POSIX.1-2001, C89 | Yes |
| [ferror](https://man7.org/linux/man-pages/man3/ferror.3.html) | `<stdio.h>` | Test the error indicator for the stream | POSIX.1-2001, C89 | Yes |
| [clearerr](https://man7.org/linux/man-pages/man3/clearerr.3.html) | `<stdio.h>` | Clear the end-of-file and error indicators for the stream | POSIX.1-2001, C89 | Yes |

<br >

---

## Character & String (string.h, ctype.h)

### Character Classification

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [isalnum](https://man7.org/linux/man-pages/man3/isalnum.3.html) | `<ctype.h>` | Check for an alphanumeric character | POSIX.1-2001, C89 | Yes |
| [isalpha](https://man7.org/linux/man-pages/man3/isalpha.3.html) | `<ctype.h>` | Check for an alphabetic character | POSIX.1-2001, C89 | Yes |
| [isascii](https://man7.org/linux/man-pages/man3/isascii.3.html) | `<ctype.h>` | Check whether c is a 7-bit unsigned char value that fits into the ASCII character set | BSD, POSIX.1-2001 | Yes |
| [isblank](https://man7.org/linux/man-pages/man3/isblank.3.html) | `<ctype.h>` | Check for a blank character; that is, a space or a tab | POSIX.1-2001, C99 | Yes |
| [iscntrl](https://man7.org/linux/man-pages/man3/iscntrl.3.html) | `<ctype.h>` | Check for a control character | POSIX.1-2001, C89 | Yes |
| [isdigit](https://man7.org/linux/man-pages/man3/isdigit.3.html) | `<ctype.h>` | Check for a digit (0 through 9) | POSIX.1-2001, C89 | Yes |
| [isgraph](https://man7.org/linux/man-pages/man3/isgraph.3.html) | `<ctype.h>` | Check for any printable character except space | POSIX.1-2001, C89 | Yes |
| [islower](https://man7.org/linux/man-pages/man3/islower.3.html) | `<ctype.h>` | Check for a lowercase character | POSIX.1-2001, C89 | Yes |
| [isprint](https://man7.org/linux/man-pages/man3/isprint.3.html) | `<ctype.h>` | Check for any printable character including space | POSIX.1-2001, C89 | Yes |
| [ispunct](https://man7.org/linux/man-pages/man3/ispunct.3.html) | `<ctype.h>` | Check for any printable character which is not a space or an alphanumeric character | POSIX.1-2001, C89 | Yes |
| [isspace](https://man7.org/linux/man-pages/man3/isspace.3.html) | `<ctype.h>` | Check for white-space characters | POSIX.1-2001, C89 | Yes |
| [isupper](https://man7.org/linux/man-pages/man3/isupper.3.html) | `<ctype.h>` | Check for an uppercase letter | POSIX.1-2001, C89 | Yes |
| [isxdigit](https://man7.org/linux/man-pages/man3/isxdigit.3.html) | `<ctype.h>` | Check for hexadecimal digits | POSIX.1-2001, C89 | Yes |
| [tolower](https://man7.org/linux/man-pages/man3/tolower.3.html) | `<ctype.h>` | Convert c to lowercase if possible | POSIX.1-2001, C89 | Yes |
| [toupper](https://man7.org/linux/man-pages/man3/toupper.3.html) | `<ctype.h>` | Convert c to uppercase if possible | POSIX.1-2001, C89 | Yes |

### String Operations

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [strcpy](https://man7.org/linux/man-pages/man3/strcpy.3.html) | `<string.h>` | Copy the string pointed to by src, including the terminating null byte | POSIX.1-2001, C89 | Yes |
| [strncpy](https://man7.org/linux/man-pages/man3/strncpy.3.html) | `<string.h>` | Copy at most n bytes of src to dest | POSIX.1-2001, C89 | Yes |
| [strcat](https://man7.org/linux/man-pages/man3/strcat.3.html) | `<string.h>` | Append the src string to the dest string | POSIX.1-2001, C89 | Yes |
| [strncat](https://man7.org/linux/man-pages/man3/strncat.3.html) | `<string.h>` | Append at most n bytes of src to dest | POSIX.1-2001, C89 | Yes |
| [strcmp](https://man7.org/linux/man-pages/man3/strcmp.3.html) | `<string.h>` | Compare the two strings s1 and s2 | POSIX.1-2001, C89 | Yes |
| [strncmp](https://man7.org/linux/man-pages/man3/strncmp.3.html) | `<string.h>` | Compare the two strings s1 and s2, comparing at most n bytes | POSIX.1-2001, C89 | Yes |
| [strcasecmp](https://man7.org/linux/man-pages/man3/strcasecmp.3.html) | `<strings.h>` | Compare two strings ignoring case | POSIX.1-2001, 4.4BSD | Yes |
| [strncasecmp](https://man7.org/linux/man-pages/man3/strncasecmp.3.html) | `<strings.h>` | Compare two strings ignoring case, at most n bytes | POSIX.1-2001, 4.4BSD | Yes |
| [strcoll](https://man7.org/linux/man-pages/man3/strcoll.3.html) | `<string.h>` | Compare two strings according to the current locale | POSIX.1-2001, C89 | Yes |
| [strxfrm](https://man7.org/linux/man-pages/man3/strxfrm.3.html) | `<string.h>` | Transform src string so result of strcmp on two transformed strings gives same result as strcoll on originals | POSIX.1-2001, C89 | Yes |
| [strchr](https://man7.org/linux/man-pages/man3/strchr.3.html) | `<string.h>` | Return a pointer to the first occurrence of the character c in the string s | POSIX.1-2001, C89 | Yes |
| [strrchr](https://man7.org/linux/man-pages/man3/strrchr.3.html) | `<string.h>` | Return a pointer to the last occurrence of the character c in the string s | POSIX.1-2001, C89 | Yes |
| [strpbrk](https://man7.org/linux/man-pages/man3/strpbrk.3.html) | `<string.h>` | Locate the first occurrence in the string s of any of the bytes in the string accept | POSIX.1-2001, C89 | Yes |
| [strcspn](https://man7.org/linux/man-pages/man3/strcspn.3.html) | `<string.h>` | Get length of a prefix substring consisting of bytes not in reject | POSIX.1-2001, C89 | Yes |
| [strspn](https://man7.org/linux/man-pages/man3/strspn.3.html) | `<string.h>` | Get length of a prefix substring consisting of bytes in accept | POSIX.1-2001, C89 | Yes |
| [strstr](https://man7.org/linux/man-pages/man3/strstr.3.html) | `<string.h>` | Finds the first occurrence of the substring needle in the string haystack | POSIX.1-2001, C89 | Yes |
| [strtok](https://man7.org/linux/man-pages/man3/strtok.3.html) | `<string.h>` | Extract tokens from strings | POSIX.1-2001, C89 | No (race:strtok) |
| [strtok_r](https://man7.org/linux/man-pages/man3/strtok_r.3.html) | `<string.h>` | Reentrant version of strtok | POSIX.1-2001, C99 | Yes |
| [strlen](https://man7.org/linux/man-pages/man3/strlen.3.html) | `<string.h>` | Calculate the length of the string pointed to by s, excluding the terminating null byte | POSIX.1-2001, C89 | Yes |
| [strnlen](https://man7.org/linux/man-pages/man3/strnlen.3.html) | `<string.h>` | Determine the length of the string pointed to by s, excluding the terminating null byte, but not beyond n | POSIX.1-2008 | Yes |
| [strdup](https://man7.org/linux/man-pages/man3/strdup.3.html) | `<string.h>` | Return a pointer to a new string which is a duplicate of the string s | POSIX.1-2001 | Yes |
| [strndup](https://man7.org/linux/man-pages/man3/strndup.3.html) | `<string.h>` | Return a pointer to a new string which is a duplicate of the string s, but not more than n bytes | POSIX.1-2008 | Yes |
| [strerror](https://man7.org/linux/man-pages/man3/strerror.3.html) | `<string.h>` | Return a pointer to the textual representation of the current errno code | POSIX.1-2001, C89 | No (race:strerror locale) |
| [strerror_r](https://man7.org/linux/man-pages/man3/strerror_r.3.html) | `<string.h>` | Reentrant version of strerror | POSIX.1-2001 | Yes |
| [strsignal](https://man7.org/linux/man-pages/man3/strsignal.3.html) | `<string.h>` | Return string describing signal number | POSIX.1-2008 | Yes |
| [strfmon](https://man7.org/linux/man-pages/man3/strfmon.3.html) | `<monetary.h>` | Format a monetary value according to the locale | POSIX.1-2008 | Yes |

### Memory Operations

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [memcpy](https://man7.org/linux/man-pages/man3/memcpy.3.html) | `<string.h>` | Copy n bytes from memory area src to memory area dest | POSIX.1-2001, C89 | Yes |
| [memmove](https://man7.org/linux/man-pages/man3/memmove.3.html) | `<string.h>` | Copy n bytes from src to dest; the memory areas may overlap | POSIX.1-2001, C89 | Yes |
| [memset](https://man7.org/linux/man-pages/man3/memset.3.html) | `<string.h>` | Fill the first n bytes of the memory area pointed to by s with the constant byte c | POSIX.1-2001, C89 | Yes |
| [memchr](https://man7.org/linux/man-pages/man3/memchr.3.html) | `<string.h>` | Scan the initial n bytes of the memory area pointed to by s for the first instance of c | POSIX.1-2001, C89 | Yes |
| [memrchr](https://man7.org/linux/man-pages/man3/memrchr.3.html) | `<string.h>` | Scan the n bytes of the memory area s for the last instance of c | GNU | Yes |
| [memcmp](https://man7.org/linux/man-pages/man3/memcmp.3.html) | `<string.h>` | Compare the first n bytes (each interpreted as unsigned char) of the memory areas s1 and s2 | POSIX.1-2001, C89 | Yes |
| [bcopy](https://man7.org/linux/man-pages/man3/bcopy.3.html) | `<strings.h>` | Copy n bytes from src to dest | 4.3BSD | Yes |
| [bzero](https://man7.org/linux/man-pages/man3/bzero.3.html) | `<strings.h>` | Set the first n bytes of the byte area starting at s to zero | 4.3BSD | Yes |
| [bcmp](https://man7.org/linux/man-pages/man3/bcmp.3.html) | `<strings.h>` | Compare the first n bytes of the two byte areas s1 and s2 | 4.3BSD | Yes |
| [swab](https://man7.org/linux/man-pages/man3/swab.3.html) | `<string.h>` | Swap adjacent bytes | POSIX.1-2001 | Yes |

<br >

---

## Memory Management (stdlib.h, sys/mman.h)

### Dynamic Memory Allocation

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [malloc](https://man7.org/linux/man-pages/man3/malloc.3.html) | `<stdlib.h>` | Allocate size bytes and return a pointer to the allocated memory | POSIX.1-2001, C89 | Yes |
| [calloc](https://man7.org/linux/man-pages/man3/calloc.3.html) | `<stdlib.h>` | Allocate memory for an array of nmemb elements of size bytes each and returns a pointer to the allocated memory | POSIX.1-2001, C89 | Yes |
| [realloc](https://man7.org/linux/man-pages/man3/realloc.3.html) | `<stdlib.h>` | Change the size of the memory block pointed to by ptr to size bytes | POSIX.1-2001, C89 | Yes |
| [reallocarray](https://man7.org/linux/man-pages/man3/reallocarray.3.html) | `<stdlib.h>` | Reallocate array, same as realloc(nmemb*size) with overflow protection | GNU | Yes |
| [free](https://man7.org/linux/man-pages/man3/free.3.html) | `<stdlib.h>` | Frees the memory space pointed to by ptr | POSIX.1-2001, C89 | Yes |
| [posix_memalign](https://man7.org/linux/man-pages/man3/posix_memalign.3.html) | `<stdlib.h>` | Allocate aligned memory, aligned to a boundary that is a multiple of alignment | POSIX.1-2001 | Yes |
| [aligned_alloc](https://man7.org/linux/man-pages/man3/aligned_alloc.3.html) | `<stdlib.h>` | Allocate size bytes of memory aligned to alignment | C11, POSIX.1-2008 | Yes |
| [memalign](https://man7.org/linux/man-pages/man3/memalign.3.html) | `<stdlib.h>` | Allocate size bytes and return a pointer to the allocated memory; memory address is a multiple of alignment | BSD, SVID | Yes |
| [valloc](https://man7.org/linux/man-pages/man3/valloc.3.html) | `<stdlib.h>` | Allocates size bytes and returns a pointer to the allocated memory; memory address is a multiple of the page size | BSD | Yes |
| [pvalloc](https://man7.org/linux/man-pages/man3/pvalloc.3.html) | `<stdlib.h>` | Allocate size bytes and returns a pointer to the allocated memory; size is rounded up to next multiple of page size | GNU | Yes |
| [mallopt](https://man7.org/linux/man-pages/man3/mallopt.3.html) | `<malloc.h>` | Set tunable parameters that affect the behavior of malloc | GNU | Yes |
| [malloc_stats](https://man7.org/linux/man-pages/man3/malloc_stats.3.html) | `<malloc.h>` | Print (on stderr) statistics about calls to malloc and free | GNU | Yes |
| [malloc_trim](https://man7.org/linux/man-pages/man3/malloc_trim.3.html) | `<malloc.h>` | Release free pages from the top of the heap | GNU | Yes |
| [malloc_usable_size](https://man7.org/linux/man-pages/man3/malloc_usable_size.3.html) | `<malloc.h>` | Obtain size of block of memory allocated with malloc | GNU | Yes |
| [mtrace](https://man7.org/linux/man-pages/man3/mtrace.3.html) | `<mcheck.h>` | Install handlers for tracing memory allocation and deallocation | GNU | Yes |
| [muntrace](https://man7.org/linux/man-pages/man3/muntrace.3.html) | `<mcheck.h>` | Turn off memory tracing | GNU | Yes |
| [mallinfo](https://man7.org/linux/man-pages/man3/mallinfo.3.html) | `<malloc.h>` | Returns a copy of the malloc internal bookkeeping information | GNU | Yes |
| [mallinfo2](https://man7.org/linux/man-pages/man3/mallinfo2.3.html) | `<malloc.h>` | Like mallinfo but with larger fields to handle modern memory sizes | GNU | Yes |
| [mcheck](https://man7.org/linux/man-pages/man3/mcheck.3.html) | `<mcheck.h>` | Consistency check for malloc | GNU | Yes |
| [mprobe](https://man7.org/linux/man-pages/man3/mprobe.3.html) | `<mcheck.h>` | Check consistency of block pointed to by ptr | GNU | Yes |
| [alloca](https://man7.org/linux/man-pages/man3/alloca.3.html) | `<alloca.h>` | Allocate memory that is automatically freed when the function that called alloca returns | BSD, GNU | Yes |

### Memory-mapped Files

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [mmap](https://man7.org/linux/man-pages/man2/mmap.2.html) | `<sys/mman.h>` | Map files or devices into memory | POSIX.1-2001 | Yes |
| [munmap](https://man7.org/linux/man-pages/man2/munmap.2.html) | `<sys/mman.h>` | Unmap files or devices from memory | POSIX.1-2001 | Yes |
| [mprotect](https://man7.org/linux/man-pages/man2/mprotect.2.html) | `<sys/mman.h>` | Set protection on a region of memory | POSIX.1-2001 | Yes |
| [msync](https://man7.org/linux/man-pages/man2/msync.2.html) | `<sys/mman.h>` | Synchronize a file with a memory map | POSIX.1-2001 | Yes |
| [mlock](https://man7.org/linux/man-pages/man2/mlock.2.html) | `<sys/mman.h>` | Lock part of the calling process virtual address space into RAM | POSIX.1-2001 | Yes |
| [mlock2](https://man7.org/linux/man-pages/man2/mlock2.2.html) | `<sys/mman.h>` | Lock part of the calling process virtual address space into RAM with flags | Linux | Yes |
| [munlock](https://man7.org/linux/man-pages/man2/munlock.2.html) | `<sys/mman.h>` | Unlock pages in the specified address range | POSIX.1-2001 | Yes |
| [mlockall](https://man7.org/linux/man-pages/man2/mlockall.2.html) | `<sys/mman.h>` | Lock all pages mapped into the address space of the calling process | POSIX.1-2001 | Yes |
| [munlockall](https://man7.org/linux/man-pages/man2/munlockall.2.html) | `<sys/mman.h>` | Unlock all pages mapped into the address space of the calling process | POSIX.1-2001 | Yes |
| [madvise](https://man7.org/linux/man-pages/man2/madvise.2.html) | `<sys/mman.h>` | Give advice about use of memory | POSIX.1-2001 | Yes |
| [posix_madvise](https://man7.org/linux/man-pages/man3/posix_madvise.3.html) | `<sys/mman.h>` | Give advice about use of memory, same as madvise but different return value | POSIX.1-2001 | Yes |
| [mincore](https://man7.org/linux/man-pages/man2/mincore.2.html) | `<sys/mman.h>` | Determine whether pages are resident in memory | POSIX.1-2001 | Yes |
| [mremap](https://man7.org/linux/man-pages/man2/mremap.2.html) | `<sys/mman.h>` | Remap a virtual memory address, expand or shrink | Linux | Yes |
| [remap_file_pages](https://man7.org/linux/man-pages/man2/remap_file_pages.2.html) | `<sys/mman.h>` | Create a nonlinear mapping | Linux | Yes |
| [shm_open](https://man7.org/linux/man-pages/man3/shm_open.3.html) | `<sys/mman.h>` | Open a POSIX shared memory object | POSIX.1-2001 | Yes |
| [shm_unlink](https://man7.org/linux/man-pages/man3/shm_unlink.3.html) | `<sys/mman.h>` | Remove a POSIX shared memory object | POSIX.1-2001 | Yes |

### Program Address Space

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [sbrk](https://man7.org/linux/man-pages/man2/sbrk.2.html) | `<unistd.h>` | Change data segment size | BSD, SUSv1 | Yes |
| [brk](https://man7.org/linux/man-pages/man2/brk.2.html) | `<unistd.h>` | Change the location of the program break | BSD, SUSv1 | Yes |
| [getpagesize](https://man7.org/linux/man-pages/man2/getpagesize.2.html) | `<unistd.h>` | Get memory page size | POSIX.1-2001 | Yes |
| [sysconf](https://man7.org/linux/man-pages/man3/sysconf.3.html) | `<unistd.h>` | Get configuration information at runtime (including _SC_PAGESIZE) | POSIX.1-2001 | Yes |

<br >

---

## Math Library (math.h)

### Basic Math Functions

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [abs](https://man7.org/linux/man-pages/man3/abs.3.html) | `<stdlib.h>` | Compute the absolute value of the integer argument | POSIX.1-2001, C89 | Yes |
| [labs](https://man7.org/linux/man-pages/man3/labs.3.html) | `<stdlib.h>` | Compute the absolute value of the long integer argument | POSIX.1-2001, C89 | Yes |
| [llabs](https://man7.org/linux/man-pages/man3/llabs.3.html) | `<stdlib.h>` | Compute the absolute value of the long long integer argument | POSIX.1-2001, C99 | Yes |
| [imaxabs](https://man7.org/linux/man-pages/man3/imaxabs.3.html) | `<inttypes.h>` | Compute the absolute value of the intmax_t argument | POSIX.1-2001, C99 | Yes |
| [fabs](https://man7.org/linux/man-pages/man3/fabs.3.html) | `<math.h>` | Compute the absolute value of the floating-point number x | POSIX.1-2001, C89 | Yes |
| [fabsf](https://man7.org/linux/man-pages/man3/fabsf.3.html) | `<math.h>` | Compute the absolute value of the float number x | POSIX.1-2001, C99 | Yes |
| [fabsl](https://man7.org/linux/man-pages/man3/fabsl.3.html) | `<math.h>` | Compute the absolute value of the long double number x | POSIX.1-2001, C99 | Yes |
| [div](https://man7.org/linux/man-pages/man3/div.3.html) | `<stdlib.h>` | Compute the quotient and remainder of the division of the numerator by denominator | POSIX.1-2001, C89 | Yes |
| [ldiv](https://man7.org/linux/man-pages/man3/ldiv.3.html) | `<stdlib.h>` | Same as div but with long arguments | POSIX.1-2001, C89 | Yes |
| [lldiv](https://man7.org/linux/man-pages/man3/lldiv.3.html) | `<stdlib.h>` | Same as div but with long long arguments | POSIX.1-2001, C99 | Yes |
| [imaxdiv](https://man7.org/linux/man-pages/man3/imaxdiv.3.html) | `<inttypes.h>` | Same as div but with intmax_t arguments | POSIX.1-2001, C99 | Yes |

### Trigonometric Functions

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [sin](https://man7.org/linux/man-pages/man3/sin.3.html) | `<math.h>` | Sine function | POSIX.1-2001, C89 | Yes |
| [cos](https://man7.org/linux/man-pages/man3/cos.3.html) | `<math.h>` | Cosine function | POSIX.1-2001, C89 | Yes |
| [tan](https://man7.org/linux/man-pages/man3/tan.3.html) | `<math.h>` | Tangent function | POSIX.1-2001, C89 | Yes |
| [asin](https://man7.org/linux/man-pages/man3/asin.3.html) | `<math.h>` | Arc sine function | POSIX.1-2001, C89 | Yes |
| [acos](https://man7.org/linux/man-pages/man3/acos.3.html) | `<math.h>` | Arc cosine function | POSIX.1-2001, C89 | Yes |
| [atan](https://man7.org/linux/man-pages/man3/atan.3.html) | `<math.h>` | Arc tangent function | POSIX.1-2001, C89 | Yes |
| [atan2](https://man7.org/linux/man-pages/man3/atan2.3.html) | `<math.h>` | Arc tangent function of two variables | POSIX.1-2001, C89 | Yes |
| [sinh](https://man7.org/linux/man-pages/man3/sinh.3.html) | `<math.h>` | Hyperbolic sine function | POSIX.1-2001, C89 | Yes |
| [cosh](https://man7.org/linux/man-pages/man3/cosh.3.html) | `<math.h>` | Hyperbolic cosine function | POSIX.1-2001, C89 | Yes |
| [tanh](https://man7.org/linux/man-pages/man3/tanh.3.html) | `<math.h>` | Hyperbolic tangent function | POSIX.1-2001, C89 | Yes |
| [asinh](https://man7.org/linux/man-pages/man3/asinh.3.html) | `<math.h>` | Inverse hyperbolic sine function | POSIX.1-2001, C99 | Yes |
| [acosh](https://man7.org/linux/man-pages/man3/acosh.3.html) | `<math.h>` | Inverse hyperbolic cosine function | POSIX.1-2001, C99 | Yes |
| [atanh](https://man7.org/linux/man-pages/man3/atanh.3.html) | `<math.h>` | Inverse hyperbolic tangent function | POSIX.1-2001, C99 | Yes |

### Exponential & Logarithmic Functions

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [exp](https://man7.org/linux/man-pages/man3/exp.3.html) | `<math.h>` | Exponential function (e^x) | POSIX.1-2001, C89 | Yes |
| [exp2](https://man7.org/linux/man-pages/man3/exp2.3.html) | `<math.h>` | Base-2 exponential function (2^x) | POSIX.1-2001, C99 | Yes |
| [expm1](https://man7.org/linux/man-pages/man3/expm1.3.html) | `<math.h>` | Exponential minus 1 (e^x - 1) | POSIX.1-2001, C99 | Yes |
| [log](https://man7.org/linux/man-pages/man3/log.3.html) | `<math.h>` | Natural logarithm function (ln x) | POSIX.1-2001, C89 | Yes |
| [log2](https://man7.org/linux/man-pages/man3/log2.3.html) | `<math.h>` | Base-2 logarithm function (log2 x) | POSIX.1-2001, C99 | Yes |
| [log10](https://man7.org/linux/man-pages/man3/log10.3.html) | `<math.h>` | Base-10 logarithm function (log10 x) | POSIX.1-2001, C89 | Yes |
| [log1p](https://man7.org/linux/man-pages/man3/log1p.3.html) | `<math.h>` | Natural logarithm of 1 plus argument (ln(1+x)) | POSIX.1-2001, C99 | Yes |
| [logb](https://man7.org/linux/man-pages/man3/logb.3.html) | `<math.h>` | Extract exponent of the floating-point number | POSIX.1-2001, C99 | Yes |
| [ilogb](https://man7.org/linux/man-pages/man3/ilogb.3.html) | `<math.h>` | Return integer part of the exponent of x | POSIX.1-2001, C99 | Yes |
| [pow](https://man7.org/linux/man-pages/man3/pow.3.html) | `<math.h>` | Power function (x^y) | POSIX.1-2001, C89 | Yes |
| [sqrt](https://man7.org/linux/man-pages/man3/sqrt.3.html) | `<math.h>` | Non-negative square root function | POSIX.1-2001, C89 | Yes |
| [cbrt](https://man7.org/linux/man-pages/man3/cbrt.3.html) | `<math.h>` | Cube root function | POSIX.1-2001, C99 | Yes |
| [hypot](https://man7.org/linux/man-pages/man3/hypot.3.html) | `<math.h>` | Euclidean distance function sqrt(x^2 + y^2) | POSIX.1-2001, C89 | Yes |

### Rounding & Remainder Functions

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [ceil](https://man7.org/linux/man-pages/man3/ceil.3.html) | `<math.h>` | Smallest integral value not less than x | POSIX.1-2001, C89 | Yes |
| [floor](https://man7.org/linux/man-pages/man3/floor.3.html) | `<math.h>` | Largest integral value not greater than x | POSIX.1-2001, C89 | Yes |
| [trunc](https://man7.org/linux/man-pages/man3/trunc.3.html) | `<math.h>` | Round to integer, toward zero | POSIX.1-2001, C99 | Yes |
| [round](https://man7.org/linux/man-pages/man3/round.3.html) | `<math.h>` | Round to nearest integer, away from zero | POSIX.1-2001, C99 | Yes |
| [lround](https://man7.org/linux/man-pages/man3/lround.3.html) | `<math.h>` | Round to nearest integer, away from zero; return long | POSIX.1-2001, C99 | Yes |
| [llround](https://man7.org/linux/man-pages/man3/llround.3.html) | `<math.h>` | Round to nearest integer, away from zero; return long long | POSIX.1-2001, C99 | Yes |
| [nearbyint](https://man7.org/linux/man-pages/man3/nearbyint.3.html) | `<math.h>` | Round to integer in current rounding direction | POSIX.1-2001, C99 | Yes |
| [rint](https://man7.org/linux/man-pages/man3/rint.3.html) | `<math.h>` | Round to integer in current rounding direction, raise inexact exception | POSIX.1-2001, C89 | Yes |
| [lrint](https://man7.org/linux/man-pages/man3/lrint.3.html) | `<math.h>` | Round to integer in current rounding direction, return long | POSIX.1-2001, C99 | Yes |
| [llrint](https://man7.org/linux/man-pages/man3/llrint.3.html) | `<math.h>` | Round to integer in current rounding direction, return long long | POSIX.1-2001, C99 | Yes |
| [fmod](https://man7.org/linux/man-pages/man3/fmod.3.html) | `<math.h>` | Floating-point remainder function | POSIX.1-2001, C89 | Yes |
| [remainder](https://man7.org/linux/man-pages/man3/remainder.3.html) | `<math.h>` | IEEE remainder function | POSIX.1-2001, C89 | Yes |
| [remquo](https://man7.org/linux/man-pages/man3/remquo.3.html) | `<math.h>` | Compute remainder and part of quotient | POSIX.1-2001, C99 | Yes |
| [modf](https://man7.org/linux/man-pages/man3/modf.3.html) | `<math.h>` | Break x into fractional and integer parts | POSIX.1-2001, C89 | Yes |
| [frexp](https://man7.org/linux/man-pages/man3/frexp.3.html) | `<math.h>` | Convert floating-point number to fractional and integral components | POSIX.1-2001, C89 | Yes |
| [ldexp](https://man7.org/linux/man-pages/man3/ldexp.3.html) | `<math.h>` | Multiply floating-point number by integral power of 2 | POSIX.1-2001, C89 | Yes |
| [scalbn](https://man7.org/linux/man-pages/man3/scalbn.3.html) | `<math.h>` | Multiply floating-point number by integral power of FLT_RADIX | POSIX.1-2001, C89 | Yes |
| [scalbln](https://man7.org/linux/man-pages/man3/scalbln.3.html) | `<math.h>` | Multiply floating-point number by integral power of FLT_RADIX, using long exponent | POSIX.1-2001, C99 | Yes |

### Classification & Comparison

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [isnan](https://man7.org/linux/man-pages/man3/isnan.3.html) | `<math.h>` | Determine whether floating-point value is not a number | POSIX.1-2001, C99 | Yes |
| [isinf](https://man7.org/linux/man-pages/man3/isinf.3.html) | `<math.h>` | Determine whether floating-point value is infinite | POSIX.1-2001, C99 | Yes |
| [isfinite](https://man7.org/linux/man-pages/man3/isfinite.3.html) | `<math.h>` | Determine whether floating-point value is a finite number | POSIX.1-2001, C99 | Yes |
| [signbit](https://man7.org/linux/man-pages/man3/signbit.3.html) | `<math.h>` | Test the sign bit of the floating-point value | POSIX.1-2001, C99 | Yes |
| [fpclassify](https://man7.org/linux/man-pages/man3/fpclassify.3.html) | `<math.h>` | Classify real floating type | POSIX.1-2001, C99 | Yes |
| [isnormal](https://man7.org/linux/man-pages/man3/isnormal.3.html) | `<math.h>` | Test whether value is a normal number | POSIX.1-2001, C99 | Yes |
| [copysign](https://man7.org/linux/man-pages/man3/copysign.3.html) | `<math.h>` | Copy sign of a number | POSIX.1-2001, C99 | Yes |
| [nextafter](https://man7.org/linux/man-pages/man3/nextafter.3.html) | `<math.h>` | Next representable floating-point value | POSIX.1-2001, C99 | Yes |
| [nexttoward](https://man7.org/linux/man-pages/man3/nexttoward.3.html) | `<math.h>` | Next representable floating-point value toward x in the direction of y | POSIX.1-2001, C99 | Yes |
| [nan](https://man7.org/linux/man-pages/man3/nan.3.html) | `<math.h>` | Return quiet NaN | POSIX.1-2001, C99 | Yes |
| [fmax](https://man7.org/linux/man-pages/man3/fmax.3.html) | `<math.h>` | Determine maximum of two floating-point numbers | POSIX.1-2001, C99 | Yes |
| [fmin](https://man7.org/linux/man-pages/man3/fmin.3.html) | `<math.h>` | Determine minimum of two floating-point numbers | POSIX.1-2001, C99 | Yes |
| [fdim](https://man7.org/linux/man-pages/man3/fdim.3.html) | `<math.h>` | Compute positive difference of two floating-point numbers | POSIX.1-2001, C99 | Yes |
| [fma](https://man7.org/linux/man-pages/man3/fma.3.html) | `<math.h>` | Floating-point multiply and add | POSIX.1-2001, C99 | Yes |

### Error & Special Functions

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [erf](https://man7.org/linux/man-pages/man3/erf.3.html) | `<math.h>` | Error function | POSIX.1-2001, C99 | Yes |
| [erfc](https://man7.org/linux/man-pages/man3/erfc.3.html) | `<math.h>` | Complementary error function | POSIX.1-2001, C99 | Yes |
| [lgamma](https://man7.org/linux/man-pages/man3/lgamma.3.html) | `<math.h>` | Natural logarithm of the absolute value of the gamma function | POSIX.1-2001, C99 | Yes |
| [tgamma](https://man7.org/linux/man-pages/man3/tgamma.3.html) | `<math.h>` | True gamma function | POSIX.1-2001, C99 | Yes |
| [j0](https://man7.org/linux/man-pages/man3/j0.3.html) | `<math.h>` | Bessel function of the first kind, order 0 | POSIX.1-2001 | Yes |
| [j1](https://man7.org/linux/man-pages/man3/j1.3.html) | `<math.h>` | Bessel function of the first kind, order 1 | POSIX.1-2001 | Yes |
| [jn](https://man7.org/linux/man-pages/man3/jn.3.html) | `<math.h>` | Bessel function of the first kind, order n | POSIX.1-2001 | Yes |
| [y0](https://man7.org/linux/man-pages/man3/y0.3.html) | `<math.h>` | Bessel function of the second kind, order 0 | POSIX.1-2001 | Yes |
| [y1](https://man7.org/linux/man-pages/man3/y1.3.html) | `<math.h>` | Bessel function of the second kind, order 1 | POSIX.1-2001 | Yes |
| [yn](https://man7.org/linux/man-pages/man3/yn.3.html) | `<math.h>` | Bessel function of the second kind, order n | POSIX.1-2001 | Yes |

### Floating-Point Environment

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [feclearexcept](https://man7.org/linux/man-pages/man3/feclearexcept.3.html) | `<fenv.h>` | Clear the supported exceptions represented by the excepts argument | POSIX.1-2001, C99 | Yes |
| [fegetexceptflag](https://man7.org/linux/man-pages/man3/fegetexceptflag.3.html) | `<fenv.h>` | Store implementation-defined representation of the exception flags | POSIX.1-2001, C99 | Yes |
| [feraiseexcept](https://man7.org/linux/man-pages/man3/feraiseexcept.3.html) | `<fenv.h>` | Raise the supported floating-point exceptions represented by excepts | POSIX.1-2001, C99 | Yes |
| [fesetexceptflag](https://man7.org/linux/man-pages/man3/fesetexceptflag.3.html) | `<fenv.h>` | Set complete status flags | POSIX.1-2001, C99 | Yes |
| [fetestexcept](https://man7.org/linux/man-pages/man3/fetestexcept.3.html) | `<fenv.h>` | Determine which of a specified subset of the floating-point exception flags are currently set | POSIX.1-2001, C99 | Yes |
| [fegetround](https://man7.org/linux/man-pages/man3/fegetround.3.html) | `<fenv.h>` | Get the rounding direction | POSIX.1-2001, C99 | Yes |
| [fesetround](https://man7.org/linux/man-pages/man3/fesetround.3.html) | `<fenv.h>` | Set the rounding direction | POSIX.1-2001, C99 | Yes |
| [fegetenv](https://man7.org/linux/man-pages/man3/fegetenv.3.html) | `<fenv.h>` | Get the floating-point environment | POSIX.1-2001, C99 | Yes |
| [feholdexcept](https://man7.org/linux/man-pages/man3/feholdexcept.3.html) | `<fenv.h>` | Save the current floating-point environment | POSIX.1-2001, C99 | Yes |
| [fesetenv](https://man7.org/linux/man-pages/man3/fesetenv.3.html) | `<fenv.h>` | Establish the floating-point environment represented by envp | POSIX.1-2001, C99 | Yes |
| [feupdateenv](https://man7.org/linux/man-pages/man3/feupdateenv.3.html) | `<fenv.h>` | Update the floating-point environment | POSIX.1-2001, C99 | Yes |

<br >

---

## Time & Date (time.h, sys/time.h)

### Time Functions

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [time](https://man7.org/linux/man-pages/man2/time.2.html) | `<time.h>` | Return the time as seconds since the Epoch (00:00:00 UTC, January 1, 1970) | POSIX.1-2001, C89 | Yes |
| [gettimeofday](https://man7.org/linux/man-pages/man2/gettimeofday.2.html) | `<sys/time.h>` | Get the time (seconds and microseconds) | POSIX.1-2001, 4.3BSD | Yes |
| [settimeofday](https://man7.org/linux/man-pages/man2/settimeofday.2.html) | `<sys/time.h>` | Set the system time | POSIX.1-2001, 4.3BSD | Yes |
| [clock_gettime](https://man7.org/linux/man-pages/man2/clock_gettime.2.html) | `<time.h>` | Find the resolution (precision) of the specified clock clk_id | POSIX.1-2001 | Yes |
| [clock_getres](https://man7.org/linux/man-pages/man2/clock_getres.2.html) | `<time.h>` | Find the resolution of the specified clock | POSIX.1-2001 | Yes |
| [clock_settime](https://man7.org/linux/man-pages/man2/clock_settime.2.html) | `<time.h>` | Set the time of the specified clock | POSIX.1-2001 | Yes |
| [clock](https://man7.org/linux/man-pages/man3/clock.3.html) | `<time.h>` | Approximate processor time used by the program | POSIX.1-2001, C89 | Yes |
| [times](https://man7.org/linux/man-pages/man3/times.3.html) | `<sys/times.h>` | Return the current process times | POSIX.1-2001, C89 | Yes |
| [difftime](https://man7.org/linux/man-pages/man3/difftime.3.html) | `<time.h>` | Calculate the difference between two times | POSIX.1-2001, C89 | Yes |
| [mktime](https://man7.org/linux/man-pages/man3/mktime.3.html) | `<time.h>` | Convert a broken-down time structure to time_t (local time) | POSIX.1-2001, C89 | Yes |
| [nanosleep](https://man7.org/linux/man-pages/man2/nanosleep.2.html) | `<time.h>` | High-resolution sleep | POSIX.1 | Yes |

### Date & Time Formatting

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [strftime](https://man7.org/linux/man-pages/man3/strftime.3.html) | `<time.h>` | Format broken-down time into a string according to format specification | POSIX.1-2001, C89 | Yes |
| [strptime](https://man7.org/linux/man-pages/man3/strptime.3.html) | `<time.h>` | Convert a string representation of time to a time tm structure | POSIX.1-2001 | Yes |
| [asctime](https://man7.org/linux/man-pages/man3/asctime.3.html) | `<time.h>` | Convert broken-down time to a string | POSIX.1-2001, C89 | Yes |
| [asctime_r](https://man7.org/linux/man-pages/man3/asctime_r.3.html) | `<time.h>` | Reentrant version of asctime | POSIX.1-2001, C89 | Yes |
| [ctime](https://man7.org/linux/man-pages/man3/ctime.3.html) | `<time.h>` | Convert calendar time to a string | POSIX.1-2001, C89 | Yes |
| [ctime_r](https://man7.org/linux/man-pages/man3/ctime_r.3.html) | `<time.h>` | Reentrant version of ctime | POSIX.1-2001 | Yes |
| [gmtime](https://man7.org/linux/man-pages/man3/gmtime.3.html) | `<time.h>` | Convert calendar time to broken-down time (UTC) | POSIX.1-2001, C89 | Yes |
| [gmtime_r](https://man7.org/linux/man-pages/man3/gmtime_r.3.html) | `<time.h>` | Reentrant version of gmtime | POSIX.1-2001 | Yes |
| [localtime](https://man7.org/linux/man-pages/man3/localtime.3.html) | `<time.h>` | Convert calendar time to broken-down time (local timezone) | POSIX.1-2001, C89 | Yes |
| [localtime_r](https://man7.org/linux/man-pages/man3/localtime_r.3.html) | `<time.h>` | Reentrant version of localtime | POSIX.1-2001 | Yes |
| [tzset](https://man7.org/linux/man-pages/man3/tzset.3.html) | `<time.h>` | Initialize time conversion information using the TZ environment variable | POSIX.1-2001, C89 | Yes |

### Timers

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [timer_create](https://man7.org/linux/man-pages/man2/timer_create.2.html) | `<time.h>` | Create a POSIX per-process timer | POSIX.1-2001 | Yes |
| [timer_delete](https://man7.org/linux/man-pages/man2/timer_delete.2.html) | `<time.h>` | Delete a POSIX per-process timer | POSIX.1-2001 | Yes |
| [timer_getoverrun](https://man7.org/linux/man-pages/man2/timer_getoverrun.2.html) | `<time.h>` | Get the timer overrun count | POSIX.1-2001 | Yes |
| [timer_gettime](https://man7.org/linux/man-pages/man2/timer_gettime.2.html) | `<time.h>` | Fetch the timer current value and interval | POSIX.1-2001 | Yes |
| [timer_settime](https://man7.org/linux/man-pages/man2/timer_settime.2.html) | `<time.h>` | Arm or disarm a timer | POSIX.1-2001 | Yes |
| [setitimer](https://man7.org/linux/man-pages/man2/setitimer.2.html) | `<sys/time.h>` | Set the value of an interval timer | POSIX.1-2001, 4.3BSD | Yes |
| [getitimer](https://man7.org/linux/man-pages/man2/getitimer.2.html) | `<sys/time.h>` | Get the value of an interval timer | POSIX.1-2001, 4.3BSD | Yes |
| [alarm](https://man7.org/linux/man-pages/man2/alarm.2.html) | `<unistd.h>` | Arrange for a SIGALRM signal to be delivered to the calling process | POSIX.1-2001 | Yes |
| [sleep](https://man7.org/linux/man-pages/man3/sleep.3.html) | `<unistd.h>` | Sleep for the specified number of seconds | POSIX.1-2001 | Yes |
| [usleep](https://man7.org/linux/man-pages/man3/usleep.3.html) | `<unistd.h>` | Suspend execution for microsecond intervals | 4.3BSD | Yes |

<br >

---

## File System (unistd.h, sys/stat.h, fcntl.h, dirent.h)

### File Information

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [stat](https://man7.org/linux/man-pages/man2/stat.2.html) | `<sys/stat.h>` | Obtain information about a file | POSIX.1-2001 | Yes |
| [fstat](https://man7.org/linux/man-pages/man2/fstat.2.html) | `<sys/stat.h>` | Obtain information about a file via file descriptor | POSIX.1-2001 | Yes |
| [lstat](https://man7.org/linux/man-pages/man2/lstat.2.html) | `<sys/stat.h>` | Obtain information about a file or symbolic link | POSIX.1-2001 | Yes |
| [statx](https://man7.org/linux/man-pages/man2/statx.2.html) | `<sys/stat.h>` | Get file status (extended) | Linux | Yes |
| [access](https://man7.org/linux/man-pages/man2/access.2.html) | `<unistd.h>` | Check real user's permissions for a file | POSIX.1-2001 | Yes |
| [faccessat](https://man7.org/linux/man-pages/man2/faccessat.2.html) | `<unistd.h>` | Check permissions of a file relative to a directory file descriptor | POSIX.1-2008 | Yes |
| [umask](https://man7.org/linux/man-pages/man2/umask.2.html) | `<sys/stat.h>` | Set the file mode creation mask | POSIX.1-2001 | Yes |

### File Operations

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [unlink](https://man7.org/linux/man-pages/man2/unlink.2.html) | `<unistd.h>` | Remove a file or directory | POSIX.1-2001 | Yes |
| [unlinkat](https://man7.org/linux/man-pages/man2/unlinkat.2.html) | `<unistd.h>` | Remove a file or directory relative to a directory file descriptor | POSIX.1-2008 | Yes |
| [rename](https://man7.org/linux/man-pages/man2/rename.2.html) | `<stdio.h>` | Change the name or location of a file | POSIX.1-2001 | Yes |
| [renameat](https://man7.org/linux/man-pages/man2/renameat.2.html) | `<stdio.h>` | Change the name or location of a file relative to directory file descriptors | POSIX.1-2008 | Yes |
| [link](https://man7.org/linux/man-pages/man2/link.2.html) | `<unistd.h>` | Create a new hard link to an existing file | POSIX.1-2001 | Yes |
| [linkat](https://man7.org/linux/man-pages/man2/linkat.2.html) | `<unistd.h>` | Create a link relative to directory file descriptors | POSIX.1-2008 | Yes |
| [symlink](https://man7.org/linux/man-pages/man2/symlink.2.html) | `<unistd.h>` | Create a symbolic link | POSIX.1-2001 | Yes |
| [symlinkat](https://man7.org/linux/man-pages/man2/symlinkat.2.html) | `<unistd.h>` | Create a symbolic link relative to a directory file descriptor | POSIX.1-2008 | Yes |
| [readlink](https://man7.org/linux/man-pages/man2/readlink.2.html) | `<unistd.h>` | Read the target of a symbolic link | POSIX.1-2001 | Yes |
| [readlinkat](https://man7.org/linux/man-pages/man2/readlinkat.2.html) | `<unistd.h>` | Read the target of a symbolic link relative to a directory file descriptor | POSIX.1-2008 | Yes |
| [truncate](https://man7.org/linux/man-pages/man2/truncate.2.html) | `<unistd.h>` | Truncate a file to a specified length | POSIX.1-2001 | Yes |
| [ftruncate](https://man7.org/linux/man-pages/man2/ftruncate.2.html) | `<unistd.h>` | Truncate a file referenced by file descriptor | POSIX.1-2001 | Yes |

### Directories

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [mkdir](https://man7.org/linux/man-pages/man2/mkdir.2.html) | `<sys/stat.h>` | Create a new directory | POSIX.1-2001 | Yes |
| [mkdirat](https://man7.org/linux/man-pages/man2/mkdirat.2.html) | `<sys/stat.h>` | Create a directory relative to a directory file descriptor | POSIX.1-2008 | Yes |
| [rmdir](https://man7.org/linux/man-pages/man2/rmdir.2.html) | `<unistd.h>` | Remove a directory if it is empty | POSIX.1-2001 | Yes |
| [chdir](https://man7.org/linux/man-pages/man2/chdir.2.html) | `<unistd.h>` | Change the working directory | POSIX.1-2001 | Yes |
| [fchdir](https://man7.org/linux/man-pages/man2/fchdir.2.html) | `<unistd.h>` | Change working directory via file descriptor | POSIX.1-2001 | Yes |
| [getcwd](https://man7.org/linux/man-pages/man3/getcwd.3.html) | `<unistd.h>` | Get the current working directory pathname | POSIX.1-2001 | Yes |
| [getwd](https://man7.org/linux/man-pages/man3/getwd.3.html) | `<unistd.h>` | Get current working directory pathname (legacy) | 4.3BSD, POSIX.1-2001 | Yes |
| [chroot](https://man7.org/linux/man-pages/man2/chroot.2.html) | `<unistd.h>` | Change the root directory | BSD, SUSv2 | Yes |
| [opendir](https://man7.org/linux/man-pages/man3/opendir.3.html) | `<dirent.h>` | Open a directory stream | POSIX.1-2001 | Yes |
| [fdopendir](https://man7.org/linux/man-pages/man3/fdopendir.3.html) | `<dirent.h>` | Open a directory stream given a file descriptor | POSIX.1-2008 | Yes |
| [closedir](https://man7.org/linux/man-pages/man3/closedir.3.html) | `<dirent.h>` | Close a directory stream | POSIX.1-2001 | Yes |
| [readdir](https://man7.org/linux/man-pages/man3/readdir.3.html) | `<dirent.h>` | Read a directory entry from a directory stream | POSIX.1-2001 | Yes |
| [readdir_r](https://man7.org/linux/man-pages/man3/readdir_r.3.html) | `<dirent.h>` | Reentrant version of readdir | POSIX.1-2001 | Yes |
| [telldir](https://man7.org/linux/man-pages/man3/telldir.3.html) | `<dirent.h>` | Return the current location in a directory stream | POSIX.1-2001 | Yes |
| [seekdir](https://man7.org/linux/man-pages/man3/seekdir.3.html) | `<dirent.h>` | Set the position of the next readdir call | POSIX.1-2001 | Yes |
| [rewinddir](https://man7.org/linux/man-pages/man3/rewinddir.3.html) | `<dirent.h>` | Reset directory stream position to beginning | POSIX.1-2001 | Yes |
| [scandir](https://man7.org/linux/man-pages/man3/scandir.3.html) | `<dirent.h>` | Scan a directory for matching entries | BSD, POSIX.1-2008 | Yes |
| [dirfd](https://man7.org/linux/man-pages/man3/dirfd.3.html) | `<dirent.h>` | Get the file descriptor associated with a directory stream | BSD, POSIX.1-2008 | Yes |

### File Ownership & Permissions

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [chmod](https://man7.org/linux/man-pages/man2/chmod.2.html) | `<sys/stat.h>` | Change file permissions | POSIX.1-2001 | Yes |
| [fchmod](https://man7.org/linux/man-pages/man2/fchmod.2.html) | `<sys/stat.h>` | Change file permissions via file descriptor | POSIX.1-2001 | Yes |
| [fchmodat](https://man7.org/linux/man-pages/man2/fchmodat.2.html) | `<sys/stat.h>` | Change file permissions relative to directory file descriptor | POSIX.1-2008 | Yes |
| [chown](https://man7.org/linux/man-pages/man2/chown.2.html) | `<unistd.h>` | Change file ownership | POSIX.1-2001 | Yes |
| [fchown](https://man7.org/linux/man-pages/man2/fchown.2.html) | `<unistd.h>` | Change file ownership via file descriptor | POSIX.1-2001 | Yes |
| [lchown](https://man7.org/linux/man-pages/man2/lchown.2.html) | `<unistd.h>` | Change file ownership without following symlinks | POSIX.1-2001 | Yes |
| [fchownat](https://man7.org/linux/man-pages/man2/fchownat.2.html) | `<unistd.h>` | Change file ownership relative to directory file descriptor | POSIX.1-2008 | Yes |
| [utime](https://man7.org/linux/man-pages/man2/utime.2.html) | `<utime.h>` | Change file last access and modification times | POSIX.1-2001 | Yes |
| [utimes](https://man7.org/linux/man-pages/man2/utimes.2.html) | `<sys/time.h>` | Change file timestamps with microsecond precision | 4.3BSD, POSIX.1-2001 | Yes |
| [utimensat](https://man7.org/linux/man-pages/man2/utimensat.2.html) | `<sys/stat.h>` | Change file timestamps with nanosecond precision relative to directory fd | POSIX.1-2008 | Yes |
| [futimens](https://man7.org/linux/man-pages/man2/futimens.2.html) | `<sys/stat.h>` | Change file timestamps with nanosecond precision via file descriptor | POSIX.1-2008 | Yes |

### File Descriptor Operations

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [fcntl](https://man7.org/linux/man-pages/man2/fcntl.2.html) | `<fcntl.h>` | Manipulate a file descriptor | POSIX.1-2001 | Yes |
| [dup](https://man7.org/linux/man-pages/man2/dup.2.html) | `<unistd.h>` | Duplicate a file descriptor | POSIX.1-2001 | Yes |
| [dup2](https://man7.org/linux/man-pages/man2/dup2.2.html) | `<unistd.h>` | Duplicate a file descriptor to a specified number | POSIX.1-2001 | Yes |
| [dup3](https://man7.org/linux/man-pages/man2/dup3.2.html) | `<unistd.h>` | Duplicate a file descriptor with flags | Linux | Yes |
| [fsync](https://man7.org/linux/man-pages/man2/fsync.2.html) | `<unistd.h>` | Synchronize a file's in-core state with storage | POSIX.1-2001 | Yes |
| [fdatasync](https://man7.org/linux/man-pages/man2/fdatasync.2.html) | `<unistd.h>` | Synchronize the in-core state of a file with storage without flushing metadata | POSIX.1-2001 | Yes |
| [sync](https://man7.org/linux/man-pages/man2/sync.2.html) | `<unistd.h>` | Commit filesystem caches to disk | POSIX.1-2001 | Yes |
| [syncfs](https://man7.org/linux/man-pages/man2/syncfs.2.html) | `<unistd.h>` | Commit filesystem caches to disk for a specific filesystem | Linux | Yes |
| [flock](https://man7.org/linux/man-pages/man2/flock.2.html) | `<sys/file.h>` | Apply or remove an advisory lock on an open file | BSD, POSIX.1-2008 | Yes |

### Pathname Resolution

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [realpath](https://man7.org/linux/man-pages/man3/realpath.3.html) | `<stdlib.h>` | Return the canonicalized absolute pathname | POSIX.1-2001 | Yes |
| [basename](https://man7.org/linux/man-pages/man3/basename.3.html) | `<libgen.h>` | Strip directory and suffix from filenames | POSIX.1-2001, GNU | Yes |
| [dirname](https://man7.org/linux/man-pages/man3/dirname.3.html) | `<libgen.h>` | Strip last component from file name | POSIX.1-2001, GNU | Yes |
| [pathconf](https://man7.org/linux/man-pages/man3/pathconf.3.html) | `<unistd.h>` | Get configuration value for a pathname | POSIX.1-2001 | Yes |
| [fpathconf](https://man7.org/linux/man-pages/man3/fpathconf.3.html) | `<unistd.h>` | Get configuration value for a file descriptor | POSIX.1-2001 | Yes |

### Filesystem Information

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [statvfs](https://man7.org/linux/man-pages/man3/statvfs.3.html) | `<sys/statvfs.h>` | Get filesystem statistics | POSIX.1-2001 | Yes |
| [fstatvfs](https://man7.org/linux/man-pages/man3/fstatvfs.3.html) | `<sys/statvfs.h>` | Get filesystem statistics via file descriptor | POSIX.1-2001 | Yes |
| [statfs](https://man7.org/linux/man-pages/man2/statfs.2.html) | `<sys/vfs.h>` | Get filesystem statistics (Linux-specific) | BSD, Linux | Yes |
| [fstatfs](https://man7.org/linux/man-pages/man2/fstatfs.2.html) | `<sys/vfs.h>` | Get filesystem statistics via file descriptor (Linux-specific) | BSD, Linux | Yes |
| [mount](https://man7.org/linux/man-pages/man2/mount.2.html) | `<sys/mount.h>` | Mount filesystem | Linux, BSD | Yes |
| [umount](https://man7.org/linux/man-pages/man2/umount.2.html) | `<sys/mount.h>` | Unmount filesystem | Linux, BSD | Yes |
| [umount2](https://man7.org/linux/man-pages/man2/umount2.2.html) | `<sys/mount.h>` | Unmount filesystem with flags | Linux | Yes |

<br >

---

## Process Control (unistd.h, sys/wait.h)

### Process Creation

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [fork](https://man7.org/linux/man-pages/man2/fork.2.html) | `<unistd.h>` | Create a new process by duplicating the calling process | POSIX.1-2001 | Yes |
| [vfork](https://man7.org/linux/man-pages/man2/vfork.2.html) | `<sys/types.h>` | Create a child process and block parent | POSIX.1-2001 (marked obsolete) | Yes |
| [clone](https://man7.org/linux/man-pages/man2/clone.2.html) | `<sched.h>` | Create a child process in a Linux-specific way | Linux | Yes |
| [clone3](https://man7.org/linux/man-pages/man2/clone3.2.html) | `<sched.h>` | Create a child process (extended version) | Linux | Yes |

### Process Execution

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [execve](https://man7.org/linux/man-pages/man2/execve.2.html) | `<unistd.h>` | Execute program with environment | POSIX.1-2001 | Yes |
| [execv](https://man7.org/linux/man-pages/man3/execv.3.html) | `<unistd.h>` | Execute program | POSIX.1-2001 | Yes |
| [execvp](https://man7.org/linux/man-pages/man3/execvp.3.html) | `<unistd.h>` | Execute program with PATH lookup | POSIX.1-2001 | Yes |
| [execvpe](https://man7.org/linux/man-pages/man3/execvpe.3.html) | `<unistd.h>` | Execute program with PATH lookup and environment | GNU | Yes |
| [execl](https://man7.org/linux/man-pages/man3/execl.3.html) | `<unistd.h>` | Execute program with argument list | POSIX.1-2001 | Yes |
| [execlp](https://man7.org/linux/man-pages/man3/execlp.3.html) | `<unistd.h>` | Execute program with PATH lookup and argument list | POSIX.1-2001 | Yes |
| [execle](https://man7.org/linux/man-pages/man3/execle.3.html) | `<unistd.h>` | Execute program with argument list and environment | POSIX.1-2001 | Yes |
| [system](https://man7.org/linux/man-pages/man3/system.3.html) | `<stdlib.h>` | Execute a shell command | POSIX.1-2001 | Yes |
| [posix_spawn](https://man7.org/linux/man-pages/man3/posix_spawn.3.html) | `<spawn.h>` | Spawn a process (POSIX) | POSIX.1-2001 | Yes |
| [posix_spawnp](https://man7.org/linux/man-pages/man3/posix_spawnp.3.html) | `<spawn.h>` | Spawn a process with PATH lookup (POSIX) | POSIX.1-2001 | Yes |

### Process Termination

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [exit](https://man7.org/linux/man-pages/man3/exit.3.html) | `<stdlib.h>` | Cause normal process termination | POSIX.1-2001, C89 | Yes |
| [_exit](https://man7.org/linux/man-pages/man2/_exit.2.html) | `<unistd.h>` | Terminate the calling process immediately | POSIX.1-2001 | Yes |
| [_Exit](https://man7.org/linux/man-pages/man3/_Exit.3.html) | `<stdlib.h>` | Equivalent to _exit | POSIX.1-2001, C99 | Yes |
| [on_exit](https://man7.org/linux/man-pages/man3/on_exit.3.html) | `<stdlib.h>` | Register a function to be called at normal process termination | BSD, SVID | Yes |
| [atexit](https://man7.org/linux/man-pages/man3/atexit.3.html) | `<stdlib.h>` | Register a function to be called at normal process termination | POSIX.1-2001, C89 | Yes |
| [abort](https://man7.org/linux/man-pages/man3/abort.3.html) | `<stdlib.h>` | Cause abnormal process termination | POSIX.1-2001, C89 | Yes |

### Process Identification

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [getpid](https://man7.org/linux/man-pages/man2/getpid.2.html) | `<unistd.h>` | Return process ID (PID) | POSIX.1-2001 | Yes |
| [getppid](https://man7.org/linux/man-pages/man2/getppid.2.html) | `<unistd.h>` | Return parent process ID | POSIX.1-2001 | Yes |
| [getpgrp](https://man7.org/linux/man-pages/man2/getpgrp.2.html) | `<unistd.h>` | Return the process group ID of the calling process | POSIX.1-2001 | Yes |
| [setpgrp](https://man7.org/linux/man-pages/man2/setpgrp.2.html) | `<unistd.h>` | Set process group ID | POSIX.1-2001 | Yes |
| [getsid](https://man7.org/linux/man-pages/man2/getsid.2.html) | `<unistd.h>` | Get session ID | POSIX.1-2001 | Yes |
| [setsid](https://man7.org/linux/man-pages/man2/setsid.2.html) | `<unistd.h>` | Create session and set process group ID | POSIX.1-2001 | Yes |
| [gettid](https://man7.org/linux/man-pages/man2/gettid.2.html) | `<unistd.h>` | Get thread identification (Linux) | Linux | Yes |

### Process Waiting

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [wait](https://man7.org/linux/man-pages/man2/wait.2.html) | `<sys/wait.h>` | Wait for process to change state | POSIX.1-2001 | Yes |
| [waitpid](https://man7.org/linux/man-pages/man2/waitpid.2.html) | `<sys/wait.h>` | Wait for a specific process to change state | POSIX.1-2001 | Yes |
| [wait3](https://man7.org/linux/man-pages/man2/wait3.2.html) | `<sys/wait.h>` | Wait for process to change state with resource usage info | BSD, SVID | Yes |
| [wait4](https://man7.org/linux/man-pages/man2/wait4.2.html) | `<sys/wait.h>` | Wait for a specific process to change state with resource usage info | BSD, SVID | Yes |
| [waitid](https://man7.org/linux/man-pages/man2/waitid.2.html) | `<sys/wait.h>` | Wait for a child process to change state (extended) | POSIX.1-2001 | Yes |
| [WIFEXITED](https://man7.org/linux/man-pages/man2/wait.2.html) | `<sys/wait.h>` | Test whether child process terminated normally | POSIX.1-2001 | Yes |
| [WIFSIGNALED](https://man7.org/linux/man-pages/man2/wait.2.html) | `<sys/wait.h>` | Test whether child process was terminated by a signal | POSIX.1-2001 | Yes |
| [WIFSTOPPED](https://man7.org/linux/man-pages/man2/wait.2.html) | `<sys/wait.h>` | Test whether child process was stopped | POSIX.1-2001 | Yes |
| [WEXITSTATUS](https://man7.org/linux/man-pages/man2/wait.2.html) | `<sys/wait.h>` | Get the child process exit status | POSIX.1-2001 | Yes |
| [WTERMSIG](https://man7.org/linux/man-pages/man2/wait.2.html) | `<sys/wait.h>` | Get the signal that caused the child to terminate | POSIX.1-2001 | Yes |

### Process Scheduling & Priority

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [nice](https://man7.org/linux/man-pages/man2/nice.2.html) | `<unistd.h>` | Change process priority | POSIX.1-2001 | Yes |
| [getpriority](https://man7.org/linux/man-pages/man2/getpriority.2.html) | `<sys/resource.h>` | Get program scheduling priority | POSIX.1-2001, BSD | Yes |
| [setpriority](https://man7.org/linux/man-pages/man2/setpriority.2.html) | `<sys/resource.h>` | Set program scheduling priority | POSIX.1-2001, BSD | Yes |
| [sched_setaffinity](https://man7.org/linux/man-pages/man2/sched_setaffinity.2.html) | `<sched.h>` | Set a thread CPU affinity mask | Linux | Yes |
| [sched_getaffinity](https://man7.org/linux/man-pages/man2/sched_getaffinity.2.html) | `<sched.h>` | Get a thread CPU affinity mask | Linux | Yes |
| [sched_setattr](https://man7.org/linux/man-pages/man2/sched_setattr.2.html) | `<sched.h>` | Set scheduling policy and attributes | Linux | Yes |
| [sched_getattr](https://man7.org/linux/man-pages/man2/sched_getattr.2.html) | `<sched.h>` | Get scheduling policy and attributes | Linux | Yes |
| [sched_yield](https://man7.org/linux/man-pages/man2/sched_yield.2.html) | `<sched.h>` | Yield the processor | POSIX.1-2001 | Yes |
| [sched_get_priority_max](https://man7.org/linux/man-pages/man2/sched_get_priority_max.2.html) | `<sched.h>` | Get maximum priority | POSIX.1-2001 | Yes |
| [sched_get_priority_min](https://man7.org/linux/man-pages/man2/sched_get_priority_min.2.html) | `<sched.h>` | Get minimum priority | POSIX.1-2001 | Yes |

### Resource Limits

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [getrlimit](https://man7.org/linux/man-pages/man2/getrlimit.2.html) | `<sys/resource.h>` | Get resource limits | POSIX.1-2001 | Yes |
| [setrlimit](https://man7.org/linux/man-pages/man2/setrlimit.2.html) | `<sys/resource.h>` | Set resource limits | POSIX.1-2001 | Yes |
| [prlimit](https://man7.org/linux/man-pages/man2/prlimit.2.html) | `<sys/resource.h>` | Get and set resource limits of an arbitrary process | Linux | Yes |
| [getrusage](https://man7.org/linux/man-pages/man2/getrusage.2.html) | `<sys/resource.h>` | Get resource usage statistics | POSIX.1-2001, BSD | Yes |
| [ulimit](https://man7.org/linux/man-pages/man3/ulimit.3.html) | `<ulimit.h>` | Get and set user limits | POSIX.1-2001 (obsolete) | Yes |

<br >

---

## Signal Handling (signal.h)

### Signal Operations

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [signal](https://man7.org/linux/man-pages/man2/signal.2.html) | `<signal.h>` | Signal management (simple) | POSIX.1-2001, C89 | Yes |
| [sigaction](https://man7.org/linux/man-pages/man2/sigaction.2.html) | `<signal.h>` | Signal management with extended options | POSIX.1-2001 | Yes |
| [kill](https://man7.org/linux/man-pages/man2/kill.2.html) | `<signal.h>` | Send a signal to a process or process group | POSIX.1-2001 | Yes |
| [killpg](https://man7.org/linux/man-pages/man3/killpg.3.html) | `<signal.h>` | Send a signal to a process group | BSD, POSIX.1-2001 | Yes |
| [raise](https://man7.org/linux/man-pages/man3/raise.3.html) | `<signal.h>` | Send a signal to the calling thread | POSIX.1-2001, C89 | Yes |
| [pthread_kill](https://man7.org/linux/man-pages/man3/pthread_kill.3.html) | `<signal.h>` | Send a signal to a thread | POSIX.1-2001 | Yes |
| [tgkill](https://man7.org/linux/man-pages/man2/tgkill.2.html) | `<signal.h>` | Send a signal to a thread in a thread group | Linux | Yes |

### Signal Sets

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [sigemptyset](https://man7.org/linux/man-pages/man3/sigemptyset.3.html) | `<signal.h>` | Initialize an empty signal set | POSIX.1-2001, C89 | Yes |
| [sigfillset](https://man7.org/linux/man-pages/man3/sigfillset.3.html) | `<signal.h>` | Initialize a full signal set | POSIX.1-2001, C89 | Yes |
| [sigaddset](https://man7.org/linux/man-pages/man3/sigaddset.3.html) | `<signal.h>` | Add a signal to a signal set | POSIX.1-2001, C89 | Yes |
| [sigdelset](https://man7.org/linux/man-pages/man3/sigdelset.3.html) | `<signal.h>` | Delete a signal from a signal set | POSIX.1-2001, C89 | Yes |
| [sigismember](https://man7.org/linux/man-pages/man3/sigismember.3.html) | `<signal.h>` | Test for a signal in a signal set | POSIX.1-2001, C89 | Yes |

### Signal Masks &amp; Waiting

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [sigprocmask](https://man7.org/linux/man-pages/man2/sigprocmask.2.html) | `<signal.h>` | Examine and change blocked signals | POSIX.1-2001 | Yes |
| [pthread_sigmask](https://man7.org/linux/man-pages/man3/pthread_sigmask.3.html) | `<signal.h>` | Examine and change blocked signals for thread | POSIX.1-2001 | Yes |
| [sigsuspend](https://man7.org/linux/man-pages/man2/sigsuspend.2.html) | `<signal.h>` | Wait for a signal | POSIX.1-2001 | Yes |
| [sigwait](https://man7.org/linux/man-pages/man3/sigwait.3.html) | `<signal.h>` | Wait for a signal | POSIX.1-2001 | Yes |
| [sigwaitinfo](https://man7.org/linux/man-pages/man2/sigwaitinfo.2.html) | `<signal.h>` | Wait for queued signals synchronously | POSIX.1-2001 | Yes |
| [sigtimedwait](https://man7.org/linux/man-pages/man2/sigtimedwait.2.html) | `<signal.h>` | Wait for queued signals with timeout | POSIX.1-2001 | Yes |
| [sigpending](https://man7.org/linux/man-pages/man2/sigpending.2.html) | `<signal.h>` | Examine pending signals | POSIX.1-2001 | Yes |
| [pause](https://man7.org/linux/man-pages/man2/pause.2.html) | `<unistd.h>` | Wait for signal | POSIX.1-2001 | Yes |

### Signal Stack

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [sigaltstack](https://man7.org/linux/man-pages/man2/sigaltstack.2.html) | `<signal.h>` | Set and/or get signal stack context | POSIX.1-2001 | Yes |
| [setjmp](https://man7.org/linux/man-pages/man3/setjmp.3.html) | `<setjmp.h>` | Save stack context for non-local goto | POSIX.1-2001, C89 | Yes |
| [longjmp](https://man7.org/linux/man-pages/man3/longjmp.3.html) | `<setjmp.h>` | Non-local jump to a saved stack context | POSIX.1-2001, C89 | Yes |
| [sigsetjmp](https://man7.org/linux/man-pages/man3/sigsetjmp.3.html) | `<setjmp.h>` | Save stack context and signal mask | POSIX.1-2001 | Yes |
| [siglongjmp](https://man7.org/linux/man-pages/man3/siglongjmp.3.html) | `<setjmp.h>` | Non-local jump with signal mask restoration | POSIX.1-2001 | Yes |

### Realtime Signal Queuing

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [sigqueue](https://man7.org/linux/man-pages/man2/sigqueue.2.html) | `<signal.h>` | Queue a signal and data to a process | POSIX.1-2001 | Yes |

<br >

---

## Environment & System Info (unistd.h, sys/utsname.h)

### Environment Variables

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [getenv](https://man7.org/linux/man-pages/man3/getenv.3.html) | `<stdlib.h>` | Get value of environment variable | POSIX.1-2001, C89 | Yes |
| [setenv](https://man7.org/linux/man-pages/man3/setenv.3.html) | `<stdlib.h>` | Change or add an environment variable | POSIX.1-2001 | Yes |
| [unsetenv](https://man7.org/linux/man-pages/man3/unsetenv.3.html) | `<stdlib.h>` | Remove an environment variable | POSIX.1-2001 | Yes |
| [putenv](https://man7.org/linux/man-pages/man3/putenv.3.html) | `<stdlib.h>` | Change or add an environment variable | POSIX.1-2001 | Yes |
| [clearenv](https://man7.org/linux/man-pages/man3/clearenv.3.html) | `<stdlib.h>` | Clear the environment | GNU | Yes |

### User & Group Identification

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [getuid](https://man7.org/linux/man-pages/man2/getuid.2.html) | `<unistd.h>` | Get user identity | POSIX.1-2001 | Yes |
| [geteuid](https://man7.org/linux/man-pages/man2/geteuid.2.html) | `<unistd.h>` | Get effective user identity | POSIX.1-2001 | Yes |
| [getgid](https://man7.org/linux/man-pages/man2/getgid.2.html) | `<unistd.h>` | Get group identity | POSIX.1-2001 | Yes |
| [getegid](https://man7.org/linux/man-pages/man2/getegid.2.html) | `<unistd.h>` | Get effective group identity | POSIX.1-2001 | Yes |
| [setuid](https://man7.org/linux/man-pages/man2/setuid.2.html) | `<unistd.h>` | Set user identity | POSIX.1-2001 | Yes |
| [seteuid](https://man7.org/linux/man-pages/man2/seteuid.2.html) | `<unistd.h>` | Set effective user identity | POSIX.1-2001 | Yes |
| [setgid](https://man7.org/linux/man-pages/man2/setgid.2.html) | `<unistd.h>` | Set group identity | POSIX.1-2001 | Yes |
| [setegid](https://man7.org/linux/man-pages/man2/setegid.2.html) | `<unistd.h>` | Set effective group identity | POSIX.1-2001 | Yes |
| [setreuid](https://man7.org/linux/man-pages/man2/setreuid.2.html) | `<unistd.h>` | Set real and effective user IDs | POSIX.1-2001 | Yes |
| [setregid](https://man7.org/linux/man-pages/man2/setregid.2.html) | `<unistd.h>` | Set real and effective group IDs | POSIX.1-2001 | Yes |
| [getgroups](https://man7.org/linux/man-pages/man2/getgroups.2.html) | `<unistd.h>` | Get list of supplementary group IDs | POSIX.1-2001 | Yes |
| [setgroups](https://man7.org/linux/man-pages/man2/setgroups.2.html) | `<unistd.h>` | Set list of supplementary group IDs | BSD, SVID | Yes |
| [getlogin](https://man7.org/linux/man-pages/man3/getlogin.3.html) | `<unistd.h>` | Get username | POSIX.1-2001 | Yes |
| [getlogin_r](https://man7.org/linux/man-pages/man3/getlogin_r.3.html) | `<unistd.h>` | Get username reentrant | POSIX.1-2001 | Yes |

### System Identification

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [uname](https://man7.org/linux/man-pages/man2/uname.2.html) | `<sys/utsname.h>` | Get name and information about current kernel | POSIX.1-2001 | Yes |
| [gethostname](https://man7.org/linux/man-pages/man2/gethostname.2.html) | `<unistd.h>` | Get hostname | POSIX.1-2001, BSD | Yes |
| [sethostname](https://man7.org/linux/man-pages/man2/sethostname.2.html) | `<unistd.h>` | Set hostname | BSD, SVID | Yes |
| [getdomainname](https://man7.org/linux/man-pages/man2/getdomainname.2.html) | `<unistd.h>` | Get domain name | BSD, SVID | Yes |
| [setdomainname](https://man7.org/linux/man-pages/man2/setdomainname.2.html) | `<unistd.h>` | Set domain name | BSD, SVID | Yes |
| [sysinfo](https://man7.org/linux/man-pages/man2/sysinfo.2.html) | `<sys/sysinfo.h>` | Get overall system statistics | Linux | Yes |

### System Configuration

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [sysconf](https://man7.org/linux/man-pages/man3/sysconf.3.html) | `<unistd.h>` | Get configuration information at runtime | POSIX.1-2001 | Yes |
| [confstr](https://man7.org/linux/man-pages/man3/confstr.3.html) | `<unistd.h>` | Get configuration-dependent string values | POSIX.1-2001 | Yes |
| [getpagesize](https://man7.org/linux/man-pages/man2/getpagesize.2.html) | `<unistd.h>` | Get memory page size | POSIX.1-2001 | Yes |
| [get_phys_pages](https://man7.org/linux/man-pages/man3/get_phys_pages.3.html) | `<sys/sysinfo.h>` | Get number of physical pages | GNU | Yes |
| [get_avphys_pages](https://man7.org/linux/man-pages/man3/get_avphys_pages.3.html) | `<sys/sysinfo.h>` | Get available physical pages | GNU | Yes |

### Terminal Control

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [isatty](https://man7.org/linux/man-pages/man3/isatty.3.html) | `<unistd.h>` | Test whether a file descriptor refers to a terminal | POSIX.1-2001 | Yes |
| [ttyname](https://man7.org/linux/man-pages/man3/ttyname.3.html) | `<unistd.h>` | Return name of a terminal | POSIX.1-2001 | Yes |
| [ttyname_r](https://man7.org/linux/man-pages/man3/ttyname_r.3.html) | `<unistd.h>` | Return name of a terminal reentrant | POSIX.1-2001 | Yes |
| [ctermid](https://man7.org/linux/man-pages/man3/ctermid.3.html) | `<stdio.h>` | Get controlling terminal name | POSIX.1-2001, C89 | Yes |

### Daemon Process

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [daemon](https://man7.org/linux/man-pages/man3/daemon.3.html) | `<unistd.h>` | Run in the background as a daemon | BSD, SVID | Yes |
| [setsid](https://man7.org/linux/man-pages/man2/setsid.2.html) | `<unistd.h>` | Creates a session and sets the process group ID | POSIX.1-2001 | Yes |

<br >

---

## Error Handling (errno.h)

### Error Reporting

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [strerror](https://man7.org/linux/man-pages/man3/strerror.3.html) | `<string.h>` | Return string describing error number | POSIX.1-2001, C89 | Yes |
| [strerror_r](https://man7.org/linux/man-pages/man3/strerror_r.3.html) | `<string.h>` | Reentrant version of strerror | POSIX.1-2001 | Yes |
| [perror](https://man7.org/linux/man-pages/man3/perror.3.html) | `<stdio.h>` | Print a message describing the value of errno | POSIX.1-2001, C89 | Yes |
| [err](https://man7.org/linux/man-pages/man3/err.3.html) | `<err.h>` | Display formatted error messages | BSD | Yes |
| [errx](https://man7.org/linux/man-pages/man3/err.3.html) | `<err.h>` | Display formatted error messages without errno info | BSD | Yes |
| [warn](https://man7.org/linux/man-pages/man3/err.3.html) | `<err.h>` | Display formatted warning messages | BSD | Yes |
| [warnx](https://man7.org/linux/man-pages/man3/err.3.html) | `<err.h>` | Display formatted warning messages without errno info | BSD | Yes |
| [errno](https://man7.org/linux/man-pages/man3/errno.3.html) | `<errno.h>` | Number of last error | POSIX.1-2001, C89 | Yes |

### Program Name

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [program_invocation_name](https://man7.org/linux/man-pages/man3/program_invocation_name.3.html) | `<errno.h>` | Name used to invoke the calling program | GNU | Yes |
| [program_invocation_short_name](https://man7.org/linux/man-pages/man3/program_invocation_short_name.3.html) | `<errno.h>` | Basename of the program invocation name | GNU | Yes |
| [error](https://man7.org/linux/man-pages/man3/error.3.html) | `<error.h>` | Print error message with status | GNU | Yes |
| [error_at_line](https://man7.org/linux/man-pages/man3/error.3.html) | `<error.h>` | Print error message with file and line | GNU | Yes |

<br >

---

## Locale & Internationalization (locale.h, libintl.h, iconv.h)

### Locale Management

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [setlocale](https://man7.org/linux/man-pages/man3/setlocale.3.html) | `<locale.h>` | Set the current locale | POSIX.1-2001, C89 | Yes |
| [localeconv](https://man7.org/linux/man-pages/man3/localeconv.3.html) | `<locale.h>` | Get numeric and monetary formatting information | POSIX.1-2001, C89 | Yes |
| [uselocale](https://man7.org/linux/man-pages/man3/uselocale.3.html) | `<locale.h>` | Set locale for the calling thread | POSIX.1-2008 | Yes |
| [newlocale](https://man7.org/linux/man-pages/man3/newlocale.3.html) | `<locale.h>` | Create a new locale object | POSIX.1-2008 | Yes |
| [duplocale](https://man7.org/linux/man-pages/man3/duplocale.3.html) | `<locale.h>` | Duplicate a locale object | POSIX.1-2008 | Yes |
| [freelocale](https://man7.org/linux/man-pages/man3/freelocale.3.html) | `<locale.h>` | Free a locale object | POSIX.1-2008 | Yes |

### Message Translation (gettext)

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [gettext](https://man7.org/linux/man-pages/man3/gettext.3.html) | `<libintl.h>` | Translate a message using default domain | POSIX.1-2001 | Yes |
| [dgettext](https://man7.org/linux/man-pages/man3/dgettext.3.html) | `<libintl.h>` | Translate a message using a given domain | POSIX.1-2001 | Yes |
| [dcgettext](https://man7.org/linux/man-pages/man3/dcgettext.3.html) | `<libintl.h>` | Translate a message using given domain and category | POSIX.1-2001 | Yes |
| [ngettext](https://man7.org/linux/man-pages/man3/ngettext.3.html) | `<libintl.h>` | Translate message with plural forms | POSIX.1-2001 | Yes |
| [dngettext](https://man7.org/linux/man-pages/man3/dngettext.3.html) | `<libintl.h>` | Translate message with plural forms in given domain | POSIX.1-2001 | Yes |
| [dcngettext](https://man7.org/linux/man-pages/man3/dcngettext.3.html) | `<libintl.h>` | Translate message with plural forms given domain/category | POSIX.1-2001 | Yes |
| [textdomain](https://man7.org/linux/man-pages/man3/textdomain.3.html) | `<libintl.h>` | Set the default text domain | POSIX.1-2001 | Yes |
| [bindtextdomain](https://man7.org/linux/man-pages/man3/bindtextdomain.3.html) | `<libintl.h>` | Bind domain to directory | POSIX.1-2001 | Yes |
| [bind_textdomain_codeset](https://man7.org/linux/man-pages/man3/bind_textdomain_codeset.3.html) | `<libintl.h>` | Specify output codeset for message catalog | GNU | Yes |

### Character Encoding Conversion

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [iconv_open](https://man7.org/linux/man-pages/man3/iconv_open.3.html) | `<iconv.h>` | Allocate descriptor for character set conversion | POSIX.1-2001 | Yes |
| [iconv](https://man7.org/linux/man-pages/man3/iconv.3.html) | `<iconv.h>` | Perform character set conversion | POSIX.1-2001 | Yes |
| [iconv_close](https://man7.org/linux/man-pages/man3/iconv_close.3.html) | `<iconv.h>` | Deallocate descriptor for character set conversion | POSIX.1-2001 | Yes |

<br >

---

## Regular Expressions (regex.h)

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [regcomp](https://man7.org/linux/man-pages/man3/regcomp.3.html) | `<regex.h>` | Compile a regular expression into an executable form | POSIX.1-2001 | Yes |
| [regexec](https://man7.org/linux/man-pages/man3/regexec.3.html) | `<regex.h>` | Execute a compiled regular expression | POSIX.1-2001 | Yes |
| [regerror](https://man7.org/linux/man-pages/man3/regerror.3.html) | `<regex.h>` | Get description of error code for regex functions | POSIX.1-2001 | Yes |
| [regfree](https://man7.org/linux/man-pages/man3/regfree.3.html) | `<regex.h>` | Free memory allocated by regcomp | POSIX.1-2001 | Yes |

<br >

---

## Dynamic Linking (dlfcn.h)

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [dlopen](https://man7.org/linux/man-pages/man3/dlopen.3.html) | `<dlfcn.h>` | Open and load a dynamic shared object | POSIX.1-2001 | Yes |
| [dlclose](https://man7.org/linux/man-pages/man3/dlclose.3.html) | `<dlfcn.h>` | Close a dynamic shared object | POSIX.1-2001 | Yes |
| [dlsym](https://man7.org/linux/man-pages/man3/dlsym.3.html) | `<dlfcn.h>` | Obtain address of a symbol in a shared object | POSIX.1-2001 | Yes |
| [dlvsym](https://man7.org/linux/man-pages/man3/dlvsym.3.html) | `<dlfcn.h>` | Get versioned symbol | GNU | Yes |
| [dlerror](https://man7.org/linux/man-pages/man3/dlerror.3.html) | `<dlfcn.h>` | Get diagnostic information | POSIX.1-2001 | Yes |
| [dladdr](https://man7.org/linux/man-pages/man3/dladdr.3.html) | `<dlfcn.h>` | Translate address to symbolic information | SVID, BSD | Yes |
| [dladdr1](https://man7.org/linux/man-pages/man3/dladdr1.3.html) | `<dlfcn.h>` | Translate address to symbolic info with extra data | GNU | Yes |
| [dl_iterate_phdr](https://man7.org/linux/man-pages/man3/dl_iterate_phdr.3.html) | `<link.h>` | Walk through the program headers | GNU | Yes |
| [dlmopen](https://man7.org/linux/man-pages/man3/dlmopen.3.html) | `<dlfcn.h>` | Open a shared object in a new namespace | GNU | Yes |

<br >

---

## Threading (pthread.h)

### Thread Creation &amp; Management

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [pthread_create](https://man7.org/linux/man-pages/man3/pthread_create.3.html) | `<pthread.h>` | Create a new thread | POSIX.1-2001 | Yes |
| [pthread_exit](https://man7.org/linux/man-pages/man3/pthread_exit.3.html) | `<pthread.h>` | Terminate the calling thread | POSIX.1-2001 | Yes |
| [pthread_join](https://man7.org/linux/man-pages/man3/pthread_join.3.html) | `<pthread.h>` | Join with a terminated thread | POSIX.1-2001 | Yes |
| [pthread_detach](https://man7.org/linux/man-pages/man3/pthread_detach.3.html) | `<pthread.h>` | Detach a thread | POSIX.1-2001 | Yes |
| [pthread_self](https://man7.org/linux/man-pages/man3/pthread_self.3.html) | `<pthread.h>` | Obtain ID of the calling thread | POSIX.1-2001 | Yes |
| [pthread_equal](https://man7.org/linux/man-pages/man3/pthread_equal.3.html) | `<pthread.h>` | Compare two thread IDs | POSIX.1-2001 | Yes |
| [pthread_once](https://man7.org/linux/man-pages/man3/pthread_once.3.html) | `<pthread.h>` | Dynamic package initialization | POSIX.1-2001 | Yes |
| [pthread_cancel](https://man7.org/linux/man-pages/man3/pthread_cancel.3.html) | `<pthread.h>` | Send a cancellation request to a thread | POSIX.1-2001 | Yes |
| [pthread_setcancelstate](https://man7.org/linux/man-pages/man3/pthread_setcancelstate.3.html) | `<pthread.h>` | Set cancelability state | POSIX.1-2001 | Yes |
| [pthread_setcanceltype](https://man7.org/linux/man-pages/man3/pthread_setcanceltype.3.html) | `<pthread.h>` | Set cancelability type | POSIX.1-2001 | Yes |
| [pthread_testcancel](https://man7.org/linux/man-pages/man3/pthread_testcancel.3.html) | `<pthread.h>` | Request delivery of any pending cancellation | POSIX.1-2001 | Yes |
| [pthread_cleanup_push](https://man7.org/linux/man-pages/man3/pthread_cleanup_push.3.html) | `<pthread.h>` | Push cancellation cleanup handler | POSIX.1-2001 | Yes |
| [pthread_cleanup_pop](https://man7.org/linux/man-pages/man3/pthread_cleanup_pop.3.html) | `<pthread.h>` | Pop cancellation cleanup handler | POSIX.1-2001 | Yes |

### Thread Attributes

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [pthread_attr_init](https://man7.org/linux/man-pages/man3/pthread_attr_init.3.html) | `<pthread.h>` | Initialize thread attributes object | POSIX.1-2001 | Yes |
| [pthread_attr_destroy](https://man7.org/linux/man-pages/man3/pthread_attr_destroy.3.html) | `<pthread.h>` | Destroy thread attributes object | POSIX.1-2001 | Yes |
| [pthread_attr_setdetachstate](https://man7.org/linux/man-pages/man3/pthread_attr_setdetachstate.3.html) | `<pthread.h>` | Set detach state attribute | POSIX.1-2001 | Yes |
| [pthread_attr_getdetachstate](https://man7.org/linux/man-pages/man3/pthread_attr_getdetachstate.3.html) | `<pthread.h>` | Get detach state attribute | POSIX.1-2001 | Yes |
| [pthread_attr_setstacksize](https://man7.org/linux/man-pages/man3/pthread_attr_setstacksize.3.html) | `<pthread.h>` | Set stack size attribute | POSIX.1-2001 | Yes |
| [pthread_attr_getstacksize](https://man7.org/linux/man-pages/man3/pthread_attr_getstacksize.3.html) | `<pthread.h>` | Get stack size attribute | POSIX.1-2001 | Yes |
| [pthread_attr_setstack](https://man7.org/linux/man-pages/man3/pthread_attr_setstack.3.html) | `<pthread.h>` | Set stack address and size attributes | POSIX.1-2001 | Yes |
| [pthread_attr_getstack](https://man7.org/linux/man-pages/man3/pthread_attr_getstack.3.html) | `<pthread.h>` | Get stack address and size attributes | POSIX.1-2001 | Yes |
| [pthread_attr_setguardsize](https://man7.org/linux/man-pages/man3/pthread_attr_setguardsize.3.html) | `<pthread.h>` | Set guard size attribute | POSIX.1-2001 | Yes |
| [pthread_attr_getguardsize](https://man7.org/linux/man-pages/man3/pthread_attr_getguardsize.3.html) | `<pthread.h>` | Get guard size attribute | POSIX.1-2001 | Yes |
| [pthread_attr_setscope](https://man7.org/linux/man-pages/man3/pthread_attr_setscope.3.html) | `<pthread.h>` | Set contention scope attribute | POSIX.1-2001 | Yes |
| [pthread_attr_getscope](https://man7.org/linux/man-pages/man3/pthread_attr_getscope.3.html) | `<pthread.h>` | Get contention scope attribute | POSIX.1-2001 | Yes |
| [pthread_attr_setschedpolicy](https://man7.org/linux/man-pages/man3/pthread_attr_setschedpolicy.3.html) | `<pthread.h>` | Set scheduling policy attribute | POSIX.1-2001 | Yes |
| [pthread_attr_getschedpolicy](https://man7.org/linux/man-pages/man3/pthread_attr_getschedpolicy.3.html) | `<pthread.h>` | Get scheduling policy attribute | POSIX.1-2001 | Yes |
| [pthread_attr_setschedparam](https://man7.org/linux/man-pages/man3/pthread_attr_setschedparam.3.html) | `<pthread.h>` | Set scheduling parameter attributes | POSIX.1-2001 | Yes |
| [pthread_attr_getschedparam](https://man7.org/linux/man-pages/man3/pthread_attr_getschedparam.3.html) | `<pthread.h>` | Get scheduling parameter attributes | POSIX.1-2001 | Yes |
| [pthread_attr_setinheritsched](https://man7.org/linux/man-pages/man3/pthread_attr_setinheritsched.3.html) | `<pthread.h>` | Set inherit scheduler attribute | POSIX.1-2001 | Yes |
| [pthread_attr_getinheritsched](https://man7.org/linux/man-pages/man3/pthread_attr_getinheritsched.3.html) | `<pthread.h>` | Get inherit scheduler attribute | POSIX.1-2001 | Yes |

### Thread-Specific Data

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [pthread_key_create](https://man7.org/linux/man-pages/man3/pthread_key_create.3.html) | `<pthread.h>` | Create a thread-specific data key | POSIX.1-2001 | Yes |
| [pthread_key_delete](https://man7.org/linux/man-pages/man3/pthread_key_delete.3.html) | `<pthread.h>` | Delete a thread-specific data key | POSIX.1-2001 | Yes |
| [pthread_setspecific](https://man7.org/linux/man-pages/man3/pthread_setspecific.3.html) | `<pthread.h>` | Associate a thread-specific value with a key | POSIX.1-2001 | Yes |
| [pthread_getspecific](https://man7.org/linux/man-pages/man3/pthread_getspecific.3.html) | `<pthread.h>` | Obtain the thread-specific value for a key | POSIX.1-2001 | Yes |

<br >

---

## Synchronization Primitives

### Mutexes

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [pthread_mutex_init](https://man7.org/linux/man-pages/man3/pthread_mutex_init.3.html) | `<pthread.h>` | Initialize a mutex | POSIX.1-2001 | Yes |
| [pthread_mutex_destroy](https://man7.org/linux/man-pages/man3/pthread_mutex_destroy.3.html) | `<pthread.h>` | Destroy a mutex | POSIX.1-2001 | Yes |
| [pthread_mutex_lock](https://man7.org/linux/man-pages/man3/pthread_mutex_lock.3.html) | `<pthread.h>` | Lock a mutex | POSIX.1-2001 | Yes |
| [pthread_mutex_unlock](https://man7.org/linux/man-pages/man3/pthread_mutex_unlock.3.html) | `<pthread.h>` | Unlock a mutex | POSIX.1-2001 | Yes |
| [pthread_mutex_trylock](https://man7.org/linux/man-pages/man3/pthread_mutex_trylock.3.html) | `<pthread.h>` | Try to lock a mutex without blocking | POSIX.1-2001 | Yes |
| [pthread_mutex_timedlock](https://man7.org/linux/man-pages/man3/pthread_mutex_timedlock.3.html) | `<pthread.h>` | Lock a mutex with a timeout | POSIX.1-2001 | Yes |
| [pthread_mutexattr_init](https://man7.org/linux/man-pages/man3/pthread_mutexattr_init.3.html) | `<pthread.h>` | Initialize mutex attributes object | POSIX.1-2001 | Yes |
| [pthread_mutexattr_destroy](https://man7.org/linux/man-pages/man3/pthread_mutexattr_destroy.3.html) | `<pthread.h>` | Destroy mutex attributes object | POSIX.1-2001 | Yes |
| [pthread_mutexattr_settype](https://man7.org/linux/man-pages/man3/pthread_mutexattr_settype.3.html) | `<pthread.h>` | Set mutex type | POSIX.1-2001 | Yes |
| [pthread_mutexattr_gettype](https://man7.org/linux/man-pages/man3/pthread_mutexattr_gettype.3.html) | `<pthread.h>` | Get mutex type | POSIX.1-2001 | Yes |
| [pthread_mutexattr_setpshared](https://man7.org/linux/man-pages/man3/pthread_mutexattr_setpshared.3.html) | `<pthread.h>` | Set process-shared attribute | POSIX.1-2001 | Yes |
| [pthread_mutexattr_getpshared](https://man7.org/linux/man-pages/man3/pthread_mutexattr_getpshared.3.html) | `<pthread.h>` | Get process-shared attribute | POSIX.1-2001 | Yes |
| [pthread_mutexattr_setprotocol](https://man7.org/linux/man-pages/man3/pthread_mutexattr_setprotocol.3.html) | `<pthread.h>` | Set protocol attribute | POSIX.1-2001 | Yes |
| [pthread_mutexattr_getprotocol](https://man7.org/linux/man-pages/man3/pthread_mutexattr_getprotocol.3.html) | `<pthread.h>` | Get protocol attribute | POSIX.1-2001 | Yes |
| [pthread_mutexattr_setprioceiling](https://man7.org/linux/man-pages/man3/pthread_mutexattr_setprioceiling.3.html) | `<pthread.h>` | Set priority ceiling attribute | POSIX.1-2001 | Yes |
| [pthread_mutexattr_getprioceiling](https://man7.org/linux/man-pages/man3/pthread_mutexattr_getprioceiling.3.html) | `<pthread.h>` | Get priority ceiling attribute | POSIX.1-2001 | Yes |

### Condition Variables

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [pthread_cond_init](https://man7.org/linux/man-pages/man3/pthread_cond_init.3.html) | `<pthread.h>` | Initialize a condition variable | POSIX.1-2001 | Yes |
| [pthread_cond_destroy](https://man7.org/linux/man-pages/man3/pthread_cond_destroy.3.html) | `<pthread.h>` | Destroy a condition variable | POSIX.1-2001 | Yes |
| [pthread_cond_signal](https://man7.org/linux/man-pages/man3/pthread_cond_signal.3.html) | `<pthread.h>` | Restart one of the threads waiting on condition variable | POSIX.1-2001 | Yes |
| [pthread_cond_broadcast](https://man7.org/linux/man-pages/man3/pthread_cond_broadcast.3.html) | `<pthread.h>` | Unblock all threads currently blocked on condition variable | POSIX.1-2001 | Yes |
| [pthread_cond_wait](https://man7.org/linux/man-pages/man3/pthread_cond_wait.3.html) | `<pthread.h>` | Wait on a condition variable | POSIX.1-2001 | Yes |
| [pthread_cond_timedwait](https://man7.org/linux/man-pages/man3/pthread_cond_timedwait.3.html) | `<pthread.h>` | Wait on a condition variable with a timeout | POSIX.1-2001 | Yes |
| [pthread_condattr_init](https://man7.org/linux/man-pages/man3/pthread_condattr_init.3.html) | `<pthread.h>` | Initialize condition variable attributes object | POSIX.1-2001 | Yes |
| [pthread_condattr_destroy](https://man7.org/linux/man-pages/man3/pthread_condattr_destroy.3.html) | `<pthread.h>` | Destroy condition variable attributes object | POSIX.1-2001 | Yes |
| [pthread_condattr_setpshared](https://man7.org/linux/man-pages/man3/pthread_condattr_setpshared.3.html) | `<pthread.h>` | Set process-shared attribute | POSIX.1-2001 | Yes |
| [pthread_condattr_getpshared](https://man7.org/linux/man-pages/man3/pthread_condattr_getpshared.3.html) | `<pthread.h>` | Get process-shared attribute | POSIX.1-2001 | Yes |
| [pthread_condattr_setclock](https://man7.org/linux/man-pages/man3/pthread_condattr_setclock.3.html) | `<pthread.h>` | Set the clock selection attribute | POSIX.1-2001 | Yes |
| [pthread_condattr_getclock](https://man7.org/linux/man-pages/man3/pthread_condattr_getclock.3.html) | `<pthread.h>` | Get the clock selection attribute | POSIX.1-2001 | Yes |

### Semaphores

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [sem_init](https://man7.org/linux/man-pages/man3/sem_init.3.html) | `<semaphore.h>` | Initialize an unnamed semaphore | POSIX.1-2001 | Yes |
| [sem_destroy](https://man7.org/linux/man-pages/man3/sem_destroy.3.html) | `<semaphore.h>` | Destroy an unnamed semaphore | POSIX.1-2001 | Yes |
| [sem_wait](https://man7.org/linux/man-pages/man3/sem_wait.3.html) | `<semaphore.h>` | Lock a semaphore | POSIX.1-2001 | Yes |
| [sem_trywait](https://man7.org/linux/man-pages/man3/sem_trywait.3.html) | `<semaphore.h>` | Lock a semaphore without blocking | POSIX.1-2001 | Yes |
| [sem_timedwait](https://man7.org/linux/man-pages/man3/sem_timedwait.3.html) | `<semaphore.h>` | Lock a semaphore with a timeout | POSIX.1-2001 | Yes |
| [sem_post](https://man7.org/linux/man-pages/man3/sem_post.3.html) | `<semaphore.h>` | Unlock a semaphore | POSIX.1-2001 | Yes |
| [sem_getvalue](https://man7.org/linux/man-pages/man3/sem_getvalue.3.html) | `<semaphore.h>` | Get the value of a semaphore | POSIX.1-2001 | Yes |
| [sem_open](https://man7.org/linux/man-pages/man3/sem_open.3.html) | `<semaphore.h>` | Initialize and open a named semaphore | POSIX.1-2001 | Yes |
| [sem_close](https://man7.org/linux/man-pages/man3/sem_close.3.html) | `<semaphore.h>` | Close a named semaphore | POSIX.1-2001 | Yes |
| [sem_unlink](https://man7.org/linux/man-pages/man3/sem_unlink.3.html) | `<semaphore.h>` | Remove a named semaphore | POSIX.1-2001 | Yes |

### Read-Write Locks

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [pthread_rwlock_init](https://man7.org/linux/man-pages/man3/pthread_rwlock_init.3.html) | `<pthread.h>` | Initialize a read-write lock object | POSIX.1-2001 | Yes |
| [pthread_rwlock_destroy](https://man7.org/linux/man-pages/man3/pthread_rwlock_destroy.3.html) | `<pthread.h>` | Destroy a read-write lock object | POSIX.1-2001 | Yes |
| [pthread_rwlock_rdlock](https://man7.org/linux/man-pages/man3/pthread_rwlock_rdlock.3.html) | `<pthread.h>` | Lock a read-write lock object for reading | POSIX.1-2001 | Yes |
| [pthread_rwlock_tryrdlock](https://man7.org/linux/man-pages/man3/pthread_rwlock_tryrdlock.3.html) | `<pthread.h>` | Lock a read-write lock for reading without blocking | POSIX.1-2001 | Yes |
| [pthread_rwlock_timedrdlock](https://man7.org/linux/man-pages/man3/pthread_rwlock_timedrdlock.3.html) | `<pthread.h>` | Lock a read-write lock for reading with timeout | POSIX.1-2001 | Yes |
| [pthread_rwlock_wrlock](https://man7.org/linux/man-pages/man3/pthread_rwlock_wrlock.3.html) | `<pthread.h>` | Lock a read-write lock object for writing | POSIX.1-2001 | Yes |
| [pthread_rwlock_trywrlock](https://man7.org/linux/man-pages/man3/pthread_rwlock_trywrlock.3.html) | `<pthread.h>` | Lock a read-write lock for writing without blocking | POSIX.1-2001 | Yes |
| [pthread_rwlock_timedwrlock](https://man7.org/linux/man-pages/man3/pthread_rwlock_timedwrlock.3.html) | `<pthread.h>` | Lock a read-write lock for writing with timeout | POSIX.1-2001 | Yes |
| [pthread_rwlock_unlock](https://man7.org/linux/man-pages/man3/pthread_rwlock_unlock.3.html) | `<pthread.h>` | Unlock a read-write lock object | POSIX.1-2001 | Yes |
| [pthread_rwlockattr_init](https://man7.org/linux/man-pages/man3/pthread_rwlockattr_init.3.html) | `<pthread.h>` | Initialize the read-write lock attributes object | POSIX.1-2001 | Yes |
| [pthread_rwlockattr_destroy](https://man7.org/linux/man-pages/man3/pthread_rwlockattr_destroy.3.html) | `<pthread.h>` | Destroy the read-write lock attributes object | POSIX.1-2001 | Yes |

### Spinlocks

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [pthread_spin_init](https://man7.org/linux/man-pages/man3/pthread_spin_init.3.html) | `<pthread.h>` | Initialize a spin lock object | POSIX.1-2001 | Yes |
| [pthread_spin_destroy](https://man7.org/linux/man-pages/man3/pthread_spin_destroy.3.html) | `<pthread.h>` | Destroy a spin lock object | POSIX.1-2001 | Yes |
| [pthread_spin_lock](https://man7.org/linux/man-pages/man3/pthread_spin_lock.3.html) | `<pthread.h>` | Lock a spin lock object | POSIX.1-2001 | Yes |
| [pthread_spin_trylock](https://man7.org/linux/man-pages/man3/pthread_spin_trylock.3.html) | `<pthread.h>` | Lock a spin lock object without blocking | POSIX.1-2001 | Yes |
| [pthread_spin_unlock](https://man7.org/linux/man-pages/man3/pthread_spin_unlock.3.html) | `<pthread.h>` | Unlock a spin lock object | POSIX.1-2001 | Yes |

### Barriers

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [pthread_barrier_init](https://man7.org/linux/man-pages/man3/pthread_barrier_init.3.html) | `<pthread.h>` | Initialize a barrier object | POSIX.1-2001 | Yes |
| [pthread_barrier_destroy](https://man7.org/linux/man-pages/man3/pthread_barrier_destroy.3.html) | `<pthread.h>` | Destroy a barrier object | POSIX.1-2001 | Yes |
| [pthread_barrier_wait](https://man7.org/linux/man-pages/man3/pthread_barrier_wait.3.html) | `<pthread.h>` | Synchronize at a barrier | POSIX.1-2001 | Yes |
| [pthread_barrierattr_init](https://man7.org/linux/man-pages/man3/pthread_barrierattr_init.3.html) | `<pthread.h>` | Initialize barrier attributes object | POSIX.1-2001 | Yes |
| [pthread_barrierattr_destroy](https://man7.org/linux/man-pages/man3/pthread_barrierattr_destroy.3.html) | `<pthread.h>` | Destroy barrier attributes object | POSIX.1-2001 | Yes |

### Thread Signals

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [pthread_sigmask](https://man7.org/linux/man-pages/man3/pthread_sigmask.3.html) | `<signal.h>` | Examine and change blocked signals | POSIX.1-2001 | Yes |
| [pthread_kill](https://man7.org/linux/man-pages/man3/pthread_kill.3.html) | `<signal.h>` | Send a signal to a thread | POSIX.1-2001 | Yes |
| [sigwait](https://man7.org/linux/man-pages/man3/sigwait.3.html) | `<signal.h>` | Wait for a signal | POSIX.1-2001 | Yes |

<br >

---

## Networking & Sockets (sys/socket.h, netinet/in.h, arpa/inet.h, netdb.h)

### Socket Creation &amp; Management

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [socket](https://man7.org/linux/man-pages/man2/socket.2.html) | `<sys/socket.h>` | Create an endpoint for communication | POSIX.1-2001 | Yes |
| [socketpair](https://man7.org/linux/man-pages/man2/socketpair.2.html) | `<sys/socket.h>` | Create a pair of connected sockets | POSIX.1-2001 | Yes |
| [bind](https://man7.org/linux/man-pages/man2/bind.2.html) | `<sys/socket.h>` | Bind a name to a socket | POSIX.1-2001 | Yes |
| [listen](https://man7.org/linux/man-pages/man2/listen.2.html) | `<sys/socket.h>` | Listen for connections on a socket | POSIX.1-2001 | Yes |
| [accept](https://man7.org/linux/man-pages/man2/accept.2.html) | `<sys/socket.h>` | Accept a connection on a socket | POSIX.1-2001 | Yes |
| [accept4](https://man7.org/linux/man-pages/man2/accept4.2.html) | `<sys/socket.h>` | Accept a connection with flags | Linux | Yes |
| [connect](https://man7.org/linux/man-pages/man2/connect.2.html) | `<sys/socket.h>` | Initiate a connection on a socket | POSIX.1-2001 | Yes |
| [shutdown](https://man7.org/linux/man-pages/man2/shutdown.2.html) | `<sys/socket.h>` | Shut down part of a full-duplex connection | POSIX.1-2001 | Yes |
| [close](https://man7.org/linux/man-pages/man2/close.2.html) | `<unistd.h>` | Close a file descriptor | POSIX.1-2001 | Yes |
| [getsockname](https://man7.org/linux/man-pages/man2/getsockname.2.html) | `<sys/socket.h>` | Get socket name | POSIX.1-2001 | Yes |
| [getpeername](https://man7.org/linux/man-pages/man2/getpeername.2.html) | `<sys/socket.h>` | Get name of connected peer | POSIX.1-2001 | Yes |

### Socket I/O

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [send](https://man7.org/linux/man-pages/man2/send.2.html) | `<sys/socket.h>` | Send a message on a socket | POSIX.1-2001 | Yes |
| [sendto](https://man7.org/linux/man-pages/man2/sendto.2.html) | `<sys/socket.h>` | Send a message on a socket to a specified address | POSIX.1-2001 | Yes |
| [sendmsg](https://man7.org/linux/man-pages/man2/sendmsg.2.html) | `<sys/socket.h>` | Send a message on a socket with control data | POSIX.1-2001 | Yes |
| [sendmmsg](https://man7.org/linux/man-pages/man2/sendmmsg.2.html) | `<sys/socket.h>` | Send multiple messages on a socket | Linux | Yes |
| [recv](https://man7.org/linux/man-pages/man2/recv.2.html) | `<sys/socket.h>` | Receive a message from a socket | POSIX.1-2001 | Yes |
| [recvfrom](https://man7.org/linux/man-pages/man2/recvfrom.2.html) | `<sys/socket.h>` | Receive a message from a socket with source address | POSIX.1-2001 | Yes |
| [recvmsg](https://man7.org/linux/man-pages/man2/recvmsg.2.html) | `<sys/socket.h>` | Receive a message with ancillary data from a socket | POSIX.1-2001 | Yes |
| [recvmmsg](https://man7.org/linux/man-pages/man2/recvmmsg.2.html) | `<sys/socket.h>` | Receive multiple messages on a socket | Linux | Yes |

### Socket Options

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [setsockopt](https://man7.org/linux/man-pages/man2/setsockopt.2.html) | `<sys/socket.h>` | Set socket options | POSIX.1-2001 | Yes |
| [getsockopt](https://man7.org/linux/man-pages/man2/getsockopt.2.html) | `<sys/socket.h>` | Get socket options | POSIX.1-2001 | Yes |
| [ioctl](https://man7.org/linux/man-pages/man2/ioctl.2.html) | `<sys/ioctl.h>` | Control device | POSIX.1-2001 | Yes |
| [fcntl](https://man7.org/linux/man-pages/man2/fcntl.2.html) | `<fcntl.h>` | Manipulate file descriptor | POSIX.1-2001 | Yes |

### Byte Order Conversion

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [htons](https://man7.org/linux/man-pages/man3/htons.3.html) | `<arpa/inet.h>` | Convert host byte order to network byte order (short) | POSIX.1-2001 | Yes |
| [htonl](https://man7.org/linux/man-pages/man3/htonl.3.html) | `<arpa/inet.h>` | Convert host byte order to network byte order (long) | POSIX.1-2001 | Yes |
| [ntohs](https://man7.org/linux/man-pages/man3/ntohs.3.html) | `<arpa/inet.h>` | Convert network byte order to host byte order (short) | POSIX.1-2001 | Yes |
| [ntohl](https://man7.org/linux/man-pages/man3/ntohl.3.html) | `<arpa/inet.h>` | Convert network byte order to host byte order (long) | POSIX.1-2001 | Yes |

### IP Address Conversion

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [inet_addr](https://man7.org/linux/man-pages/man3/inet_addr.3.html) | `<arpa/inet.h>` | Convert IPv4 address string to binary form | POSIX.1-2001 | Yes |
| [inet_aton](https://man7.org/linux/man-pages/man3/inet_aton.3.html) | `<arpa/inet.h>` | Convert IPv4 address string to binary form | BSD, POSIX.1-2001 | Yes |
| [inet_ntoa](https://man7.org/linux/man-pages/man3/inet_ntoa.3.html) | `<arpa/inet.h>` | Convert IPv4 binary address to dotted-decimal string | POSIX.1-2001 | Yes |
| [inet_pton](https://man7.org/linux/man-pages/man3/inet_pton.3.html) | `<arpa/inet.h>` | Convert IP address from presentation to network format | POSIX.1-2001 | Yes |
| [inet_ntop](https://man7.org/linux/man-pages/man3/inet_ntop.3.html) | `<arpa/inet.h>` | Convert IP address from network to presentation format | POSIX.1-2001 | Yes |

### Name Resolution (DNS)

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [gethostbyname](https://man7.org/linux/man-pages/man3/gethostbyname.3.html) | `<netdb.h>` | Get network host entry (legacy) | POSIX.1-2001 (obsolete) | Yes |
| [gethostbyaddr](https://man7.org/linux/man-pages/man3/gethostbyaddr.3.html) | `<netdb.h>` | Get network host entry by address (legacy) | POSIX.1-2001 (obsolete) | Yes |
| [getaddrinfo](https://man7.org/linux/man-pages/man3/getaddrinfo.3.html) | `<netdb.h>` | Network address and service translation | POSIX.1-2001 | Yes |
| [freeaddrinfo](https://man7.org/linux/man-pages/man3/freeaddrinfo.3.html) | `<netdb.h>` | Free addrinfo structures | POSIX.1-2001 | Yes |
| [gai_strerror](https://man7.org/linux/man-pages/man3/gai_strerror.3.html) | `<netdb.h>` | Print error messages from getaddrinfo return code | POSIX.1-2001 | Yes |
| [getnameinfo](https://man7.org/linux/man-pages/man3/getnameinfo.3.html) | `<netdb.h>` | Address-to-name translation in protocol-independent manner | POSIX.1-2001 | Yes |
| [getnetbyname](https://man7.org/linux/man-pages/man3/getnetbyname.3.html) | `<netdb.h>` | Get network entry by name | BSD, POSIX.1-2001 (obsolete) | Yes |
| [getnetbyaddr](https://man7.org/linux/man-pages/man3/getnetbyaddr.3.html) | `<netdb.h>` | Get network entry by address | BSD, POSIX.1-2001 (obsolete) | Yes |

### Service &amp; Protocol Database

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [getservbyname](https://man7.org/linux/man-pages/man3/getservbyname.3.html) | `<netdb.h>` | Get service entry by name | POSIX.1-2001 | Yes |
| [getservbyport](https://man7.org/linux/man-pages/man3/getservbyport.3.html) | `<netdb.h>` | Get service entry by port | POSIX.1-2001 | Yes |
| [getprotobyname](https://man7.org/linux/man-pages/man3/getprotobyname.3.html) | `<netdb.h>` | Get protocol entry by name | POSIX.1-2001 | Yes |
| [getprotobynumber](https://man7.org/linux/man-pages/man3/getprotobynumber.3.html) | `<netdb.h>` | Get protocol entry by number | POSIX.1-2001 | Yes |
| [setservent](https://man7.org/linux/man-pages/man3/setservent.3.html) | `<netdb.h>` | Rewind to start of services file | POSIX.1-2001 | Yes |
| [endservent](https://man7.org/linux/man-pages/man3/endservent.3.html) | `<netdb.h>` | Close services file | POSIX.1-2001 | Yes |
| [setprotoent](https://man7.org/linux/man-pages/man3/setprotoent.3.html) | `<netdb.h>` | Rewind to start of protocols file | POSIX.1-2001 | Yes |
| [endprotoent](https://man7.org/linux/man-pages/man3/endprotoent.3.html) | `<netdb.h>` | Close protocols file | POSIX.1-2001 | Yes |

### Multicast

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [if_nametoindex](https://man7.org/linux/man-pages/man3/if_nametoindex.3.html) | `<net/if.h>` | Map network interface name to index | POSIX.1-2001 | Yes |
| [if_indextoname](https://man7.org/linux/man-pages/man3/if_indextoname.3.html) | `<net/if.h>` | Map network interface index to name | POSIX.1-2001 | Yes |
| [if_nameindex](https://man7.org/linux/man-pages/man3/if_nameindex.3.html) | `<net/if.h>` | Return all network interface names and indexes | POSIX.1-2001 | Yes |
| [if_freenameindex](https://man7.org/linux/man-pages/man3/if_freenameindex.3.html) | `<net/if.h>` | Free memory allocated by if_nameindex | POSIX.1-2001 | Yes |

<br >

---

## Wide Character & Multibyte (wchar.h, wctype.h)

### Wide Character I/O

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [fgetwc](https://man7.org/linux/man-pages/man3/fgetwc.3.html) | `<wchar.h>` | Read a wide character from a stream | POSIX.1-2001, C99 | Yes |
| [getwc](https://man7.org/linux/man-pages/man3/getwc.3.html) | `<wchar.h>` | Read a wide character from a stream | POSIX.1-2001, C99 | Yes |
| [getwchar](https://man7.org/linux/man-pages/man3/getwchar.3.html) | `<wchar.h>` | Read a wide character from stdin | POSIX.1-2001, C99 | Yes |
| [fputwc](https://man7.org/linux/man-pages/man3/fputwc.3.html) | `<wchar.h>` | Write a wide character to a stream | POSIX.1-2001, C99 | Yes |
| [putwc](https://man7.org/linux/man-pages/man3/putwc.3.html) | `<wchar.h>` | Write a wide character to a stream | POSIX.1-2001, C99 | Yes |
| [putwchar](https://man7.org/linux/man-pages/man3/putwchar.3.html) | `<wchar.h>` | Write a wide character to stdout | POSIX.1-2001, C99 | Yes |
| [ungetwc](https://man7.org/linux/man-pages/man3/ungetwc.3.html) | `<wchar.h>` | Push a wide character back to an input stream | POSIX.1-2001, C99 | Yes |
| [fgetws](https://man7.org/linux/man-pages/man3/fgetws.3.html) | `<wchar.h>` | Read a wide-character string from a stream | POSIX.1-2001, C99 | Yes |
| [fputws](https://man7.org/linux/man-pages/man3/fputws.3.html) | `<wchar.h>` | Write a wide-character string to a stream | POSIX.1-2001, C99 | Yes |

### Wide Character Formatted I/O

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [wprintf](https://man7.org/linux/man-pages/man3/wprintf.3.html) | `<wchar.h>` | Write formatted wide-character output to stdout | POSIX.1-2001, C99 | Yes |
| [fwprintf](https://man7.org/linux/man-pages/man3/fwprintf.3.html) | `<wchar.h>` | Write formatted wide-character output to a stream | POSIX.1-2001, C99 | Yes |
| [swprintf](https://man7.org/linux/man-pages/man3/swprintf.3.html) | `<wchar.h>` | Write formatted wide-character output to a buffer | POSIX.1-2001, C99 | Yes |
| [vwprintf](https://man7.org/linux/man-pages/man3/vwprintf.3.html) | `<wchar.h>` | Equivalent to wprintf with variable argument list | POSIX.1-2001, C99 | Yes |
| [vfwprintf](https://man7.org/linux/man-pages/man3/vfwprintf.3.html) | `<wchar.h>` | Equivalent to fwprintf with variable argument list | POSIX.1-2001, C99 | Yes |
| [vswprintf](https://man7.org/linux/man-pages/man3/vswprintf.3.html) | `<wchar.h>` | Equivalent to swprintf with variable argument list | POSIX.1-2001, C99 | Yes |
| [wscanf](https://man7.org/linux/man-pages/man3/wscanf.3.html) | `<wchar.h>` | Read formatted wide-character input from stdin | POSIX.1-2001, C99 | Yes |
| [fwscanf](https://man7.org/linux/man-pages/man3/fwscanf.3.html) | `<wchar.h>` | Read formatted wide-character input from a stream | POSIX.1-2001, C99 | Yes |
| [swscanf](https://man7.org/linux/man-pages/man3/swscanf.3.html) | `<wchar.h>` | Read formatted wide-character input from a buffer | POSIX.1-2001, C99 | Yes |
| [vwscanf](https://man7.org/linux/man-pages/man3/vwscanf.3.html) | `<wchar.h>` | Equivalent to wscanf with variable argument list | POSIX.1-2001, C99 | Yes |
| [vfwscanf](https://man7.org/linux/man-pages/man3/vfwscanf.3.html) | `<wchar.h>` | Equivalent to fwscanf with variable argument list | POSIX.1-2001, C99 | Yes |
| [vswscanf](https://man7.org/linux/man-pages/man3/vswscanf.3.html) | `<wchar.h>` | Equivalent to swscanf with variable argument list | POSIX.1-2001, C99 | Yes |

### Wide Character String Operations

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [wcslen](https://man7.org/linux/man-pages/man3/wcslen.3.html) | `<wchar.h>` | Determine the length of a wide-character string | POSIX.1-2001, C99 | Yes |
| [wcsnlen](https://man7.org/linux/man-pages/man3/wcsnlen.3.html) | `<wchar.h>` | Determine the length of a fixed-size wide-character string | POSIX.1-2008 | Yes |
| [wcscpy](https://man7.org/linux/man-pages/man3/wcscpy.3.html) | `<wchar.h>` | Copy a wide-character string | POSIX.1-2001, C99 | Yes |
| [wcsncpy](https://man7.org/linux/man-pages/man3/wcsncpy.3.html) | `<wchar.h>` | Copy a fixed-size wide-character string | POSIX.1-2001, C99 | Yes |
| [wcscat](https://man7.org/linux/man-pages/man3/wcscat.3.html) | `<wchar.h>` | Concatenate two wide-character strings | POSIX.1-2001, C99 | Yes |
| [wcsncat](https://man7.org/linux/man-pages/man3/wcsncat.3.html) | `<wchar.h>` | Concatenate two wide-character strings with size limit | POSIX.1-2001, C99 | Yes |
| [wcscmp](https://man7.org/linux/man-pages/man3/wcscmp.3.html) | `<wchar.h>` | Compare two wide-character strings | POSIX.1-2001, C99 | Yes |
| [wcsncmp](https://man7.org/linux/man-pages/man3/wcsncmp.3.html) | `<wchar.h>` | Compare two fixed-size wide-character strings | POSIX.1-2001, C99 | Yes |
| [wcscasecmp](https://man7.org/linux/man-pages/man3/wcscasecmp.3.html) | `<wchar.h>` | Compare two wide-character strings ignoring case | POSIX.1-2008 | Yes |
| [wcsncasecmp](https://man7.org/linux/man-pages/man3/wcsncasecmp.3.html) | `<wchar.h>` | Compare two fixed-size wide-character strings ignoring case | POSIX.1-2008 | Yes |
| [wcschr](https://man7.org/linux/man-pages/man3/wcschr.3.html) | `<wchar.h>` | Search a wide character in a wide-character string | POSIX.1-2001, C99 | Yes |
| [wcsrchr](https://man7.org/linux/man-pages/man3/wcsrchr.3.html) | `<wchar.h>` | Search a wide character in a wide-character string in reverse | POSIX.1-2001, C99 | Yes |
| [wcsstr](https://man7.org/linux/man-pages/man3/wcsstr.3.html) | `<wchar.h>` | Locate a substring in a wide-character string | POSIX.1-2001, C99 | Yes |
| [wcspbrk](https://man7.org/linux/man-pages/man3/wcspbrk.3.html) | `<wchar.h>` | Search a wide-character string for any of a set of wide characters | POSIX.1-2001, C99 | Yes |
| [wcscspn](https://man7.org/linux/man-pages/man3/wcscspn.3.html) | `<wchar.h>` | Get span of wide characters not in reject string | POSIX.1-2001, C99 | Yes |
| [wcsspn](https://man7.org/linux/man-pages/man3/wcsspn.3.html) | `<wchar.h>` | Get span of wide characters in accept string | POSIX.1-2001, C99 | Yes |
| [wcstok](https://man7.org/linux/man-pages/man3/wcstok.3.html) | `<wchar.h>` | Extract tokens from a wide-character string | POSIX.1-2001, C99 | Yes |
| [wcsdup](https://man7.org/linux/man-pages/man3/wcsdup.3.html) | `<wchar.h>` | Duplicate a wide-character string | POSIX.1-2008 | Yes |

### Wide Character Classification

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [iswalpha](https://man7.org/linux/man-pages/man3/iswalpha.3.html) | `<wctype.h>` | Test for alphabetic wide character | POSIX.1-2001, C99 | Yes |
| [iswlower](https://man7.org/linux/man-pages/man3/iswlower.3.html) | `<wctype.h>` | Test for lowercase wide character | POSIX.1-2001, C99 | Yes |
| [iswupper](https://man7.org/linux/man-pages/man3/iswupper.3.html) | `<wctype.h>` | Test for uppercase wide character | POSIX.1-2001, C99 | Yes |
| [iswdigit](https://man7.org/linux/man-pages/man3/iswdigit.3.html) | `<wctype.h>` | Test for decimal digit wide character | POSIX.1-2001, C99 | Yes |
| [iswxdigit](https://man7.org/linux/man-pages/man3/iswxdigit.3.html) | `<wctype.h>` | Test for hexadecimal digit wide character | POSIX.1-2001, C99 | Yes |
| [iswspace](https://man7.org/linux/man-pages/man3/iswspace.3.html) | `<wctype.h>` | Test for whitespace wide character | POSIX.1-2001, C99 | Yes |
| [iswpunct](https://man7.org/linux/man-pages/man3/iswpunct.3.html) | `<wctype.h>` | Test for punctuation wide character | POSIX.1-2001, C99 | Yes |
| [iswalnum](https://man7.org/linux/man-pages/man3/iswalnum.3.html) | `<wctype.h>` | Test for alphanumeric wide character | POSIX.1-2001, C99 | Yes |
| [iswprint](https://man7.org/linux/man-pages/man3/iswprint.3.html) | `<wctype.h>` | Test for printing wide character | POSIX.1-2001, C99 | Yes |
| [iswgraph](https://man7.org/linux/man-pages/man3/iswgraph.3.html) | `<wctype.h>` | Test for any printable wide character except space | POSIX.1-2001, C99 | Yes |
| [iswcntrl](https://man7.org/linux/man-pages/man3/iswcntrl.3.html) | `<wctype.h>` | Test for control wide character | POSIX.1-2001, C99 | Yes |
| [iswascii](https://man7.org/linux/man-pages/man3/iswascii.3.html) | `<wctype.h>` | Test for ASCII wide character | BSD | Yes |
| [towlower](https://man7.org/linux/man-pages/man3/towlower.3.html) | `<wctype.h>` | Convert wide character to lowercase | POSIX.1-2001, C99 | Yes |
| [towupper](https://man7.org/linux/man-pages/man3/towupper.3.html) | `<wctype.h>` | Convert wide character to uppercase | POSIX.1-2001, C99 | Yes |

### Multibyte Character Conversion

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [mblen](https://man7.org/linux/man-pages/man3/mblen.3.html) | `<stdlib.h>` | Determine number of bytes in a multibyte character | POSIX.1-2001, C89 | Yes |
| [mbtowc](https://man7.org/linux/man-pages/man3/mbtowc.3.html) | `<stdlib.h>` | Convert a multibyte sequence to wide character | POSIX.1-2001, C89 | Yes |
| [wctomb](https://man7.org/linux/man-pages/man3/wctomb.3.html) | `<stdlib.h>` | Convert a wide character to a multibyte sequence | POSIX.1-2001, C89 | Yes |
| [mbstowcs](https://man7.org/linux/man-pages/man3/mbstowcs.3.html) | `<stdlib.h>` | Convert a multibyte string to a wide-character string | POSIX.1-2001, C89 | Yes |
| [wcstombs](https://man7.org/linux/man-pages/man3/wcstombs.3.html) | `<stdlib.h>` | Convert a wide-character string to a multibyte string | POSIX.1-2001, C89 | Yes |
| [mbsrtowcs](https://man7.org/linux/man-pages/man3/mbsrtowcs.3.html) | `<wchar.h>` | Convert a multibyte string to wide-character string with restart | POSIX.1-2001, C99 | Yes |
| [wcsrtombs](https://man7.org/linux/man-pages/man3/wcsrtombs.3.html) | `<wchar.h>` | Convert a wide-character string to multibyte string with restart | POSIX.1-2001, C99 | Yes |
| [mbsnrtowcs](https://man7.org/linux/man-pages/man3/mbsnrtowcs.3.html) | `<wchar.h>` | Convert a multibyte string to wide-character string with size limit | POSIX.1-2008 | Yes |
| [wcsnrtombs](https://man7.org/linux/man-pages/man3/wcsnrtombs.3.html) | `<wchar.h>` | Convert a wide-character string to multibyte with size limit | POSIX.1-2008 | Yes |
| [mbrlen](https://man7.org/linux/man-pages/man3/mbrlen.3.html) | `<wchar.h>` | Determine number of bytes in a multibyte sequence | POSIX.1-2001, C99 | Yes |
| [mbrtowc](https://man7.org/linux/man-pages/man3/mbrtowc.3.html) | `<wchar.h>` | Convert a multibyte sequence to a wide character with restart | POSIX.1-2001, C99 | Yes |
| [wcrtomb](https://man7.org/linux/man-pages/man3/wcrtomb.3.html) | `<wchar.h>` | Convert a wide character to a multibyte sequence with restart | POSIX.1-2001, C99 | Yes |

### Wide Character Numeric Conversion

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [wcstod](https://man7.org/linux/man-pages/man3/wcstod.3.html) | `<wchar.h>` | Convert wide-character string to double | POSIX.1-2001, C99 | Yes |
| [wcstof](https://man7.org/linux/man-pages/man3/wcstof.3.html) | `<wchar.h>` | Convert wide-character string to float | POSIX.1-2001, C99 | Yes |
| [wcstold](https://man7.org/linux/man-pages/man3/wcstold.3.html) | `<wchar.h>` | Convert wide-character string to long double | POSIX.1-2001, C99 | Yes |
| [wcstol](https://man7.org/linux/man-pages/man3/wcstol.3.html) | `<wchar.h>` | Convert wide-character string to long integer | POSIX.1-2001, C99 | Yes |
| [wcstoul](https://man7.org/linux/man-pages/man3/wcstoul.3.html) | `<wchar.h>` | Convert wide-character string to unsigned long integer | POSIX.1-2001, C99 | Yes |
| [wcstoll](https://man7.org/linux/man-pages/man3/wcstoll.3.html) | `<wchar.h>` | Convert wide-character string to long long integer | POSIX.1-2001, C99 | Yes |
| [wcstoull](https://man7.org/linux/man-pages/man3/wcstoull.3.html) | `<wchar.h>` | Convert wide-character string to unsigned long long | POSIX.1-2001, C99 | Yes |
| [wcstoimax](https://man7.org/linux/man-pages/man3/wcstoimax.3.html) | `<stdint.h>` | Convert wide-character string to intmax_t | POSIX.1-2001, C99 | Yes |
| [wcstoumax](https://man7.org/linux/man-pages/man3/wcstoumax.3.html) | `<stdint.h>` | Convert wide-character string to uintmax_t | POSIX.1-2001, C99 | Yes |

### Wide Character Date &amp; Time Formatting

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [wcsftime](https://man7.org/linux/man-pages/man3/wcsftime.3.html) | `<time.h>` | Format date and time for the current locale using wide characters | POSIX.1-2001, C99 | Yes |

### Wide Character Memory Operations

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [wmemcpy](https://man7.org/linux/man-pages/man3/wmemcpy.3.html) | `<wchar.h>` | Copy wide-character memory area | POSIX.1-2001, C99 | Yes |
| [wmemmove](https://man7.org/linux/man-pages/man3/wmemmove.3.html) | `<wchar.h>` | Copy wide-character memory area with possible overlap | POSIX.1-2001, C99 | Yes |
| [wmemset](https://man7.org/linux/man-pages/man3/wmemset.3.html) | `<wchar.h>` | Fill wide-character memory area with a constant wide character | POSIX.1-2001, C99 | Yes |
| [wmemchr](https://man7.org/linux/man-pages/man3/wmemchr.3.html) | `<wchar.h>` | Search a wide character in a wide-character array | POSIX.1-2001, C99 | Yes |
| [wmemcmp](https://man7.org/linux/man-pages/man3/wmemcmp.3.html) | `<wchar.h>` | Compare two wide-character memory areas | POSIX.1-2001, C99 | Yes |

<br >

---

## Complex Math (complex.h)

### Complex Arithmetic

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [cabs](https://man7.org/linux/man-pages/man3/cabs.3.html) | `<complex.h>` | Absolute value of complex number | POSIX.1-2001, C99 | Yes |
| [cabsf](https://man7.org/linux/man-pages/man3/cabsf.3.html) | `<complex.h>` | Absolute value of complex float | POSIX.1-2001, C99 | Yes |
| [cabsl](https://man7.org/linux/man-pages/man3/cabsl.3.html) | `<complex.h>` | Absolute value of complex long double | POSIX.1-2001, C99 | Yes |
| [carg](https://man7.org/linux/man-pages/man3/carg.3.html) | `<complex.h>` | Argument (phase angle) of complex number | POSIX.1-2001, C99 | Yes |
| [cargf](https://man7.org/linux/man-pages/man3/cargf.3.html) | `<complex.h>` | Argument of complex float | POSIX.1-2001, C99 | Yes |
| [cargl](https://man7.org/linux/man-pages/man3/cargl.3.html) | `<complex.h>` | Argument of complex long double | POSIX.1-2001, C99 | Yes |
| [csqrt](https://man7.org/linux/man-pages/man3/csqrt.3.html) | `<complex.h>` | Square root of complex number | POSIX.1-2001, C99 | Yes |
| [csqrtf](https://man7.org/linux/man-pages/man3/csqrtf.3.html) | `<complex.h>` | Square root of complex float | POSIX.1-2001, C99 | Yes |
| [csqrtl](https://man7.org/linux/man-pages/man3/csqrtl.3.html) | `<complex.h>` | Square root of complex long double | POSIX.1-2001, C99 | Yes |
| [cpow](https://man7.org/linux/man-pages/man3/cpow.3.html) | `<complex.h>` | Complex power function | POSIX.1-2001, C99 | Yes |
| [cpowf](https://man7.org/linux/man-pages/man3/cpowf.3.html) | `<complex.h>` | Complex power function (float) | POSIX.1-2001, C99 | Yes |
| [cpowl](https://man7.org/linux/man-pages/man3/cpowl.3.html) | `<complex.h>` | Complex power function (long double) | POSIX.1-2001, C99 | Yes |
| [cexp](https://man7.org/linux/man-pages/man3/cexp.3.html) | `<complex.h>` | Complex exponential function | POSIX.1-2001, C99 | Yes |
| [cexpf](https://man7.org/linux/man-pages/man3/cexpf.3.html) | `<complex.h>` | Complex exponential function (float) | POSIX.1-2001, C99 | Yes |
| [cexpl](https://man7.org/linux/man-pages/man3/cexpl.3.html) | `<complex.h>` | Complex exponential function (long double) | POSIX.1-2001, C99 | Yes |
| [clog](https://man7.org/linux/man-pages/man3/clog.3.html) | `<complex.h>` | Complex natural logarithm | POSIX.1-2001, C99 | Yes |
| [clogf](https://man7.org/linux/man-pages/man3/clogf.3.html) | `<complex.h>` | Complex natural logarithm (float) | POSIX.1-2001, C99 | Yes |
| [clogl](https://man7.org/linux/man-pages/man3/clogl.3.html) | `<complex.h>` | Complex natural logarithm (long double) | POSIX.1-2001, C99 | Yes |

### Complex Trigonometry

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [csin](https://man7.org/linux/man-pages/man3/csin.3.html) | `<complex.h>` | Complex sine function | POSIX.1-2001, C99 | Yes |
| [ccos](https://man7.org/linux/man-pages/man3/ccos.3.html) | `<complex.h>` | Complex cosine function | POSIX.1-2001, C99 | Yes |
| [ctan](https://man7.org/linux/man-pages/man3/ctan.3.html) | `<complex.h>` | Complex tangent function | POSIX.1-2001, C99 | Yes |
| [casin](https://man7.org/linux/man-pages/man3/casin.3.html) | `<complex.h>` | Complex arc sine function | POSIX.1-2001, C99 | Yes |
| [cacos](https://man7.org/linux/man-pages/man3/cacos.3.html) | `<complex.h>` | Complex arc cosine function | POSIX.1-2001, C99 | Yes |
| [catan](https://man7.org/linux/man-pages/man3/catan.3.html) | `<complex.h>` | Complex arc tangent function | POSIX.1-2001, C99 | Yes |
| [csinh](https://man7.org/linux/man-pages/man3/csinh.3.html) | `<complex.h>` | Complex hyperbolic sine function | POSIX.1-2001, C99 | Yes |
| [ccosh](https://man7.org/linux/man-pages/man3/ccosh.3.html) | `<complex.h>` | Complex hyperbolic cosine function | POSIX.1-2001, C99 | Yes |
| [ctanh](https://man7.org/linux/man-pages/man3/ctanh.3.html) | `<complex.h>` | Complex hyperbolic tangent function | POSIX.1-2001, C99 | Yes |
| [casinh](https://man7.org/linux/man-pages/man3/casinh.3.html) | `<complex.h>` | Complex arc hyperbolic sine function | POSIX.1-2001, C99 | Yes |
| [cacosh](https://man7.org/linux/man-pages/man3/cacosh.3.html) | `<complex.h>` | Complex arc hyperbolic cosine function | POSIX.1-2001, C99 | Yes |
| [catanh](https://man7.org/linux/man-pages/man3/catanh.3.html) | `<complex.h>` | Complex arc hyperbolic tangent function | POSIX.1-2001, C99 | Yes |

### Complex Decomposition

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [creal](https://man7.org/linux/man-pages/man3/creal.3.html) | `<complex.h>` | Get real part of complex number | POSIX.1-2001, C99 | Yes |
| [cimag](https://man7.org/linux/man-pages/man3/cimag.3.html) | `<complex.h>` | Get imaginary part of complex number | POSIX.1-2001, C99 | Yes |
| [conj](https://man7.org/linux/man-pages/man3/conj.3.html) | `<complex.h>` | Complex conjugate function | POSIX.1-2001, C99 | Yes |
| [cproj](https://man7.org/linux/man-pages/man3/cproj.3.html) | `<complex.h>` | Project into Riemann sphere | POSIX.1-2001, C99 | Yes |

<br >

---

## Searching & Sorting (stdlib.h, search.h)

### Sorting

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [qsort](https://man7.org/linux/man-pages/man3/qsort.3.html) | `<stdlib.h>` | Sort an array using quicksort algorithm | POSIX.1-2001, C89 | Yes |
| [qsort_r](https://man7.org/linux/man-pages/man3/qsort_r.3.html) | `<stdlib.h>` | Sort an array with user-supplied argument | GNU | Yes |
| [heapsort](https://man7.org/linux/man-pages/man3/heapsort.3.html) | `<search.h>` | Sort an array using heapsort algorithm | BSD | Yes |
| [mergesort](https://man7.org/linux/man-pages/man3/mergesort.3.html) | `<search.h>` | Sort an array using mergesort algorithm | BSD | Yes |

### Searching

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [bsearch](https://man7.org/linux/man-pages/man3/bsearch.3.html) | `<stdlib.h>` | Binary search a sorted array | POSIX.1-2001, C89 | Yes |
| [bsearch_r](https://man7.org/linux/man-pages/man3/bsearch_r.3.html) | `<stdlib.h>` | Binary search a sorted array with user-supplied argument | GNU | Yes |
| [lfind](https://man7.org/linux/man-pages/man3/lfind.3.html) | `<search.h>` | Linear search an array | POSIX.1-2001, SVID | Yes |
| [lsearch](https://man7.org/linux/man-pages/man3/lsearch.3.html) | `<search.h>` | Linear search an array, adding entry if not found | POSIX.1-2001, SVID | Yes |

### Hash Tables (hsearch)

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [hcreate](https://man7.org/linux/man-pages/man3/hcreate.3.html) | `<search.h>` | Create a hash table | POSIX.1-2001 | Yes |
| [hsearch](https://man7.org/linux/man-pages/man3/hsearch.3.html) | `<search.h>` | Search hash table for an entry | POSIX.1-2001 | Yes |
| [hdestroy](https://man7.org/linux/man-pages/man3/hdestroy.3.html) | `<search.h>` | Destroy a hash table | POSIX.1-2001 | Yes |
| [hcreate_r](https://man7.org/linux/man-pages/man3/hcreate_r.3.html) | `<search.h>` | Create a hash table (reentrant) | GNU | Yes |
| [hsearch_r](https://man7.org/linux/man-pages/man3/hsearch_r.3.html) | `<search.h>` | Search hash table for an entry (reentrant) | GNU | Yes |
| [hdestroy_r](https://man7.org/linux/man-pages/man3/hdestroy_r.3.html) | `<search.h>` | Destroy a hash table (reentrant) | GNU | Yes |

### Binary Search Trees (tsearch)

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [tsearch](https://man7.org/linux/man-pages/man3/tsearch.3.html) | `<search.h>` | Search a binary tree | POSIX.1-2001 | Yes |
| [tfind](https://man7.org/linux/man-pages/man3/tfind.3.html) | `<search.h>` | Find entry in binary tree without adding | POSIX.1-2001 | Yes |
| [tdelete](https://man7.org/linux/man-pages/man3/tdelete.3.html) | `<search.h>` | Delete an entry from binary tree | POSIX.1-2001 | Yes |
| [tdestroy](https://man7.org/linux/man-pages/man3/tdestroy.3.html) | `<search.h>` | Destroy entire binary tree | GNU | Yes |
| [twalk](https://man7.org/linux/man-pages/man3/twalk.3.html) | `<search.h>` | Walk a binary tree | POSIX.1-2001 | Yes |
| [twalk_r](https://man7.org/linux/man-pages/man3/twalk_r.3.html) | `<search.h>` | Walk a binary tree (reentrant) | GNU | Yes |

<br >

---

## Random Numbers (stdlib.h)

### Basic Random Number Generation

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [rand](https://man7.org/linux/man-pages/man3/rand.3.html) | `<stdlib.h>` | Generate a random integer | POSIX.1-2001, C89 | Yes |
| [srand](https://man7.org/linux/man-pages/man3/srand.3.html) | `<stdlib.h>` | Seed the random number generator | POSIX.1-2001, C89 | Yes |
| [rand_r](https://man7.org/linux/man-pages/man3/rand_r.3.html) | `<stdlib.h>` | Generate a random integer (reentrant) | POSIX.1-2001 | Yes |
| [random](https://man7.org/linux/man-pages/man3/random.3.html) | `<stdlib.h>` | Generate a random number (linear congruential) | POSIX.1-2001, BSD | Yes |
| [srandom](https://man7.org/linux/man-pages/man3/srandom.3.html) | `<stdlib.h>` | Seed random number generator | POSIX.1-2001, BSD | Yes |
| [setstate](https://man7.org/linux/man-pages/man3/setstate.3.html) | `<stdlib.h>` | Set random number generator state array | POSIX.1-2001, BSD | Yes |
| [initstate](https://man7.org/linux/man-pages/man3/initstate.3.html) | `<stdlib.h>` | Initialize random number generator state array | POSIX.1-2001, BSD | Yes |

### Advanced Random Number Generation

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [drand48](https://man7.org/linux/man-pages/man3/drand48.3.html) | `<stdlib.h>` | Generate uniformly distributed doubles | POSIX.1-2001, SVID | Yes |
| [erand48](https://man7.org/linux/man-pages/man3/erand48.3.html) | `<stdlib.h>` | Generate uniformly distributed doubles with seed | POSIX.1-2001, SVID | Yes |
| [lrand48](https://man7.org/linux/man-pages/man3/lrand48.3.html) | `<stdlib.h>` | Generate uniformly distributed long integers | POSIX.1-2001, SVID | Yes |
| [nrand48](https://man7.org/linux/man-pages/man3/nrand48.3.html) | `<stdlib.h>` | Generate uniformly distributed long integers with seed | POSIX.1-2001, SVID | Yes |
| [mrand48](https://man7.org/linux/man-pages/man3/mrand48.3.html) | `<stdlib.h>` | Generate signed long integers | POSIX.1-2001, SVID | Yes |
| [jrand48](https://man7.org/linux/man-pages/man3/jrand48.3.html) | `<stdlib.h>` | Generate signed long integers with seed | POSIX.1-2001, SVID | Yes |
| [srand48](https://man7.org/linux/man-pages/man3/srand48.3.html) | `<stdlib.h>` | Seed random number generator | POSIX.1-2001, SVID | Yes |
| [seed48](https://man7.org/linux/man-pages/man3/seed48.3.html) | `<stdlib.h>` | Seed random number generator and return previous seed | POSIX.1-2001, SVID | Yes |
| [lcong48](https://man7.org/linux/man-pages/man3/lcong48.3.html) | `<stdlib.h>` | Set random number generator parameters | POSIX.1-2001, SVID | Yes |

### Cryptographic Random Numbers

| Function | Header | Description | Standard | MT-Safe |
| --- | --- | --- | --- | --- |
| [random_get_bytes](https://man7.org/linux/man-pages/man3/random_get_bytes.3.html) | `<bsd/stdlib.h>` | Get random bytes (BSD) | BSD | Yes |
| [arc4random](https://man7.org/linux/man-pages/man3/arc4random.3.html) | `<stdlib.h>` | Pseudo-random number generator | BSD | Yes |
| [arc4random_buf](https://man7.org/linux/man-pages/man3/arc4random_buf.3.html) | `<stdlib.h>` | Fill buffer with random bytes | BSD | Yes |
| [arc4random_uniform](https://man7.org/linux/man-pages/man3/arc4random_uniform.3.html) | `<stdlib.h>` | Generate uniform random integer less than upper bound | BSD | Yes |
| [getrandom](https://man7.org/linux/man-pages/man2/getrandom.2.html) | `<sys/random.h>` | Obtain a series of random bytes (Linux) | Linux | Yes |

<br >

---

*Last updated: 2024*