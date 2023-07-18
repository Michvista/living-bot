text = '''
Every educational institution, professor, and student body holds a unique identity. Thus, educational organizations must adjust their regulations to fit the current needs of their scholars. Although prohibiting cell phone use in college courses is excessive, there are other ways to reconcile studentsâ rights with instructors' expectations. Allowing just the right amount of regulation and flexibility within colleges can cultivate an optimal learning atmosphere that ensures maximum safety for its members.

Essay prompt: Should educational institutions control cell phone usage in classes?

Cell phones have gone from a desired commodity to an essential item. While these devices offer us easy access to the rest of the world, they can cause problems for educators. High school teachers may be able to ask pupils in their classes to put away their mobiles, but should professors possess similar control over grown men and women? The solution is crafting cell phone usage rules that limit disruptions without impeding student liberties.
Continuation of the same examplesâ¦

The principal basis for restricting cell phone use in the classroom is that phones can act as a distraction. Not only do students and teachers become diverted, but this has an analogous impact on someone glancing at their device during a movie screening - even if it's silent, the illuminated display will still divert oneâs focus away from what matters most!

When debating mobile phone regulations in the classroom, safety is typically brought to the forefront. Emergencies may happen at any time and students should have their phones with them for peace of mind. Parents' needs come into play too; if a student has children, they could need access to call someone during medical emergencies. Furthermore, if an individual is on standby for work-related matters then having a cell phone accessible would be useful as well - there are endless plausible scenarios that make it difficult not to provide exceptions from these rules!

To ensure all students have an opportunity to learn without distraction, the optimal choice is to establish and enforce mobile phone usage rules. With these guidelines in place, pupils should be able to carry their devices with them as long as they remain on silent during class hours. This way, phones are easily accessible for any necessary use but don't interfere with anyone's learning experience. Vibrate settings can be allowed if the instructor feels comfortable with it, as the buzz may not be heard in a crowded classroom. In an emergency situation, students can quickly step out of class to answer their phones. This will create a more relaxed environment for both instructors and students alike.

Cell phone restrictions in the classroom should be enforced with clear and specific disciplinary measures for violations. For instance, if a student is caught using their cell phone during class, they can be excused from that day's classes. Professors should avoid seizing control of the device out of consideration for potential liability issues. Itâs safer to request students leave the classroom than take away their phones, as any damages incurred while in a professor's possession could result in liability for repairs on behalf of the school or instructor.
'''

# Split the text into chunks of 200 words
words = text.split()
chunks = [' '.join(words[i:i+200]) for i in range(0, len(words), 200)]

# Print the chunks
for chunk in chunks:
    print(chunk)
    print('---')
