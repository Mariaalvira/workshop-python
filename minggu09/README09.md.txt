#10. Brief Tour of the Standard Library
##10.1. Operating System Interface
Be sure to use the import os style instead of from os import *. This will keep os.open() from shadowing the built-in open() function which operates much differently.
##10.2. File Wildcards
##10.3. Command Line Arguments
Common utility scripts often need to process command line arguments. These arguments are stored in the sys module’s argv attribute as a list.
The argparse module provides a more sophisticated mechanism to process command line arguments. When run at the command line with python top.py --lines=5 alpha.txt beta.txt, the script sets args.lines to 5 and args.filenames to ['alpha.txt', 'beta.txt'].
##10.4. Error Output Redirection and Program Termination
The sys module also has attributes for stdin, stdout, and stderr. The latter is useful for emitting warnings and error messages to make them visible even when stdout has been redirected
##0.5. String Pattern Matching
The re module provides regular expression tools for advanced string processing. For complex matching and manipulation, regular expressions offer succinct, optimized solutions
##10.6. Mathematics
The math module gives access to the underlying C library functions for floating point math:
##10.7. Internet Access
There are a number of modules for accessing the internet and processing internet protocols. Two of the simplest are urllib.request for retrieving data from URLs and smtplib for sending mail:
##10.8. Dates and Times
The datetime module supplies classes for manipulating dates and times in both simple and complex ways. While date and time arithmetic is supported, the focus of the implementation is on efficient member extraction for output formatting and manipulation. 
##10.9. Data Compression
Common data archiving and compression formats are directly supported by modules including: zlib, gzip, bz2, lzma, zipfile and tarfile.
##10.10. Performance Measurement
Some Python users develop a deep interest in knowing the relative performance of different approaches to the same problem. Python provides a measurement tool that answers those questions immediately.
##10.11. Quality Control
One approach for developing high quality software is to write tests for each function as it is developed and to run those tests frequently during the development process.
##10.12. Batteries Included
Python has a “batteries included” philosophy. This is best seen through the sophisticated and robust capabilities of its larger packages. For example:
The xmlrpc.client and xmlrpc.server modules make implementing remote procedure calls into an almost trivial task. Despite the modules names, no direct knowledge or handling of XML is needed.
The email package is a library for managing email messages, including MIME and other RFC 2822-based message documents. Unlike smtplib and poplib which actually send and receive messages, the email package has a complete toolset for building or decoding complex message structures (including attachments) and for implementing internet encoding and header protocols.
The json package provides robust support for parsing this popular data interchange format. The csv module supports direct reading and writing of files in Comma-Separated Value format, commonly supported by databases and spreadsheets. XML processing is supported by the xml.etree.ElementTree, xml.dom and xml.sax packages. Together, these modules and packages greatly simplify data interchange between Python applications and other tools.
The sqlite3 module is a wrapper for the SQLite database library, providing a persistent database that can be updated and accessed using slightly nonstandard SQL syntax.
Internationalization is supported by a number of modules including gettext, locale, and the codecs package.

#11. Brief Tour of the Standard Library — Part II
This second tour covers more advanced modules that support professional programming needs. These modules rarely occur in small scripts.

##11.1. Output Formatting
The reprlib module provides a version of repr() customized for abbreviated displays of large or deeply nested containers
The pprint module offers more sophisticated control over printing both built-in and user defined objects in a way that is readable by the interpreter.
##11.2. Templating
The string module includes a versatile Template class with a simplified syntax suitable for editing by end-users. This allows users to customize their applications without having to alter the application.
The format uses placeholder names formed by $ with valid Python identifiers (alphanumeric characters and underscores).
##11.3. Working with Binary Data Record Layouts
The struct module provides pack() and unpack() functions for working with variable length binary record formats. The following example shows how to loop through header information in a ZIP file without using the zipfile module. Pack codes "H" and "I" represent two and four byte unsigned numbers respectively. The "<" indicates that they are standard size and in little-endian byte order
##11.4. Multi-threading
Threading is a technique for decoupling tasks which are not sequentially dependent. Threads can be used to improve the responsiveness of applications that accept user input while other tasks run in the background. A related use case is running I/O in parallel with computations in another thread.
##11.5. Logging
The logging module offers a full featured and flexible logging system. At its simplest, log messages are sent to a file or to sys.stderr
##1.6. Weak References
Python does automatic memory management (reference counting for most objects and garbage collection to eliminate cycles). The memory is freed shortly after the last reference to it has been eliminated.

This approach works fine for most applications but occasionally there is a need to track objects only as long as they are being used by something else. Unfortunately, just tracking them creates a reference that makes them permanent. The weakref module provides tools for tracking objects without creating a reference. 
##11.7. Tools for Working with Lists
Many data structure needs can be met with the built-in list type. However, sometimes there is a need for alternative implementations with different performance trade-offs.
##1.8. Decimal Floating Point Arithmetic
The decimal module offers a Decimal datatype for decimal floating point arithmetic. Compared to the built-in float implementation of binary floating point, the class is especially helpful for

financial applications and other uses which require exact decimal representation,

control over precision,

control over rounding to meet legal or regulatory requirements,

tracking of significant decimal places, or

applications where the user expects the results to match calculations done by hand.