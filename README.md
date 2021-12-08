# cmpsc101-s2021-final-project-team-10
River Magee
Griffin Wirth
5/5/21
CMPSCI 101
Final Project Progress Report
“Hidden Crypto Coded Message Project”
The project has grown exponentially since the beginning, but the beginning was a rocky
start. River is not on campus with Griffin right now so the start-up of the project was
complicated. The project idea was the first file assignment that was due from each group.
Because the group was not able to get together in person there were two different ideas for the
project. The first was a Black Jack project which fit the criteria for a potential project but lacked
creative adjustments. The next idea was Project Track 1: Cryptography and Cryptanalysis. This
project idea had more creative potential and was more computer grounded. The next assignment
was the project proposal and the group convened before that assignment was due to straightening
out their final idea for the project. The final project idea was eventually finalized as the
cryptography prompt. After that, the group was able to move on to the coding portion of the
project.
Thus far, we believe we have implemented the hardest part of our code, figuring out the
processes needed to encrypt and decrypt user input messages. It was challenging at first to
conceptualize what exactly we needed to do in order to properly and securely encrypt user data.
Initially, we tried using a method that involved converting whatever characters were given into
numerical values, that could then be shifted a few places and returned back to the user using
“Chr” and “Ord.” However, we believed that there was a more secure way of encrypting user
data using the knowledge we have acquired over the course of the class, as decrypting a message
that was only moved down four characters would be incredibly easy to figure out. So instead, we
discovered a library we could use, called cryptography, which allowed us to import certain
modules that already had built-in abilities to help us with our encryption, especially when it came
to generating hashes and keys for passwords. By using this library, we were able to create four
functions within a class, in case other programs needed to inherit what we made.
The first function, named “Generate_Key,” creates a long list of random numbers and
letters that will eventually be associated with the user's message. Next, it copies this key down
into a document designed to hold onto all the keys made for any messages. The second function,
called “Read_Key,” simply reads the key we generated from the file we placed it into. The real
heart of our program exists within the final two functions we used to encrypt and decrypt user
messages. The “encrypt_messags” function asks the user what they would like to type to have
encrypted. It then encodes the message, switching it from the data type of a string to the data
type of a byte. From this, we used the built-in function “encrypt” to transform the input message
into the key we generated. For example, the message “Hello Computer Science 101!” is
converted into:
“b'gAAAAABgkzrAlaqxT_L2GY2iGyqP63AoP0uSBKeUw6FUkfiKMgr7fWwRoROj7kmmIta
aRks_8E8pavsTu80TMQYjyrzMjRd-NAvNzFD5x7qRnTOHYi8V0uc=.”
Of course, no one is able to read the key we have made to protect and secure our message
unless they have access to the following decryption program. The function “decrypt_message”
generates a decryption key and uses it to access our original message.
We still have yet to create the structure around our program, as we want to use it in a
context that teaches the user about what it is it's doing and how it's doing it. For this part, we
were thinking of creating a way to show the user how much time it took to encrypt and decrypt
their message, and perhaps implementing the use of a password as well. For example, they type
both a message and a password, but only the password will let the program go forward with its
decryption function. This would allow for some further engagement with our program, hopefully
allowing them to use it in a real-life context. The ultimate goal we had for this project was to
hopefully use it to send encrypted messages through an email server, as suggested by the final
project sheet. This would be an awesome example of the real-world application of what we have
learned this semester, on top of being a genuinely useful program. If we are able to complete the
aforementioned structure of our program and finalize the internal working of our encryption,
then we would attempt to figure out how to send our messages through some sort of online
server to prove its security.
Looking to the future of the project, the group will implement more code to make the
code foolproof with no loopholes or ways for the code to simply not work. We will also work on
synthesizing the code to make it not as complicated to look at so that in the future it may be able
to be used for other people or other projects. The closest task ahead of the group is the
presentation of the project. In that, the code will be further examed and explained, a test run of
the code will be played out, and future plans for the code will be revealed. Until then, we’re
taking the project one code stand at a time.
cmpsc101-s2021-final-project-wirthg created by GitHub Classroom