# Summary
字符串类型的题目多以考验语法基础和字符串处理的基本操作为主，同时在日常工作中也有很多贴近实际的作用。
## Reviews
### Classic methods:
- S+S link string itself [Rotated Word]
- Sort or count char counts to determine two strings

### Grammer tips:
1. split() will split by space(not just one space)
2. strip() can cut space at head&end 
3. reversed() will have return, reverse() just reverse itself but no return.
4. islower(), upper()
5. ASCII ord('a') -32 = 'A'
6. ASCII array(127)
## Problems
1. [8. Rotate String](https://www.lintcode.com/problem/rotate-string/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0008-rotate-string.py)  
Rotate the char array in place by offset.   
The rest 'offset' numbers of char will be move to head. So classic method, link two same string and get result start from proper index.   
Make sure consider the offset more than len(array) first.  
Space O(n), Time O(n) 

2. [13. Implement strStr()](https://www.lintcode.com/problem/implement-strstr/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0013-implement-strstr.py)  
Find target string in string.  
Python has target() function, while the normal way to implement is is O($n^2$) time to  find it. KMP / Rabin Karp not considered yet.
3. [53. Reverse Words in a String](https://www.lintcode.com/problem/reverse-words-in-a-string/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0053-reverse-words-in-a-string.py)  
   Reverse words in sentence.  
4. [133. Longest Word](https://www.lintcode.com/problem/longest-word/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/133-longest-word.py)  
   record a tmp max_length, loop all words, if len(word) > max, update max_length, and empty max_words array, insert this 'new max' word.
5. [146. Lowercase to Uppercase II](https://www.lintcode.com/problem/lowercase-to-uppercase-ii/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0146-lowercase-to-uppercase-ii.py)  
char convert
6. [157. Unique Characters](https://www.lintcode.com/problem/unique-characters/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0157-unique-characters.py)  
with extra data structure, use set to comapre. Or build a ASCII array(127 all, but use 129 instead). Loop check wether the code has been used.
7. [158. Valid Anagram](https://www.lintcode.com/problem/valid-anagram/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0158-valid-anagram.py)  
anagrams problem. Stright method, sort two strings, see weather they are equal or not. But require 2 O(LogN) time at least. If require O(n) time, O(1) extra space. Just caculate each char counts in two strings, if occur diff, return false.  
8. [200. Longest Palindromic Substring](https://www.lintcode.com/problem/longest-palindromic-substring/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0200-longest-palindromic-substring.py)  
O(n2), DP lopp fiind from possible longest string is a way. 另有中心线枚举和Manacher's Algorithm in O(N) time.
9.  [209. First Unique Character in a String](https://www.lintcode.com/problem/first-unique-character-in-a-string/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0209-first-unique-character-in-a-string.py)  
hash map record each char counts, loop char in string return the fist char occur 1 time only. [?Considering Data Stream problem?]
10. [211. String Permutation](https://www.lintcode.com/problem/string-permutation/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0211-string-permutation.py)  
Sort or count char counts to determine two strings
11. [212. Space Replacement](https://www.lintcode.com/problem/space-replacement/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0212-space-replacement.py)  
Reverse Loop.
12. [241. String to Integer](https://www.lintcode.com/problem/string-to-integer/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0241-string-to-integer.py)  
start from last index to add. or use ord to determine number in char.
13. [408. Add Binary](https://www.lintcode.com/problem/add-binary/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0408-add-binary.py)  
[*Star problem in string*]reverse calc sum, not hard to come up method, but need to pay attension details.
14. [415. Valid Palindrome](https://www.lintcode.com/problem/valid-palindrome/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0415-valid-palindrome.py)  
normal way, build a clean string, jungle weather it is a paindrome string, need extra space. O(n) time without extra memory. Need use two pointers method.
15. [420. Count and Say](https://www.lintcode.com/problem/count-and-say/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0420-count-and-say.py)  
print a string as how to say it.
recursion cout and print rule string.
16. [422. Length of Last Word](https://www.lintcode.com/problem/length-of-last-word/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0422-length-of-last-word.py)  
return the length of last word.
17. [425. Letter Combinations of a Phone Number](https://www.lintcode.com/problem/letter-combinations-of-a-phone-number/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0425-letter-combinations-of-a-phone-number.py)  
DFS recursion find all possible combination.
18. [449. Char to Integer](https://www.lintcode.com/problem/char-to-integer/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0449-char-to-integer.py)  
ord() return char's ASCII
19. [478. Simple Calculator](https://www.lintcode.com/problem/simple-calculator/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0478-simple-calculator.py)  
Do as calculator.
20. [491. Palindrome Number](https://www.lintcode.com/problem/palindrome-number/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0491-palindrome-number.py)  
[*Star problem in string*]Negative is not palindrome. Some hints: 
Could negative integers be palindromes? (ie, -1) 
 If you are thinking of converting the integer to string, note the restriction of using extra space. 
You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case? 
 There is a more generic way of solving this problem.
21. [524. Left Pad](https://www.lintcode.com/problem/left-pad) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0524-left-pad.py)
build string as required.
22. [671. Rotate Words](https://www.lintcode.com/problem/rotate-words/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0671-rotate-words.py) [<b>[Review]<b>](https://dataleoz.com/lintcode-rotate-words/)  
Check rotated words. Note that use 2 string method to check rotated words will only in 2len(word) time.
23. [702. Concatenated String with Uncommon Characters of Two Strings](https://www.lintcode.com/problem/concatenated-string-with-uncommon-characters-of-two-strings/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0702-concatenated-string-with-uncommon-characters-of-two-strings.py) [<b>[Review]<b>](https://dataleoz.com/lintcode-Concatenated-String-with-Uncommon-Characters-of-Two-Strings/)  
Concatenate uncommon char in two strings.[Official answer is better]
24. [720. Rearrange a String With Integers](https://www.lintcode.com/problem/rearrange-a-string-with-integers/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0720-rearrange-a-string-with-integers.py)  
seperate deal nums and upper char, then merge
25. [891. Valid Palindrome II](https://www.lintcode.com/problem/valid-palindrome-ii/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0891-valid-palindrome-ii.py)
judge palindrome if allows to delete at most one cahr. Two pointers to jundge string, if occur not equal char, jundge delete left or right pointer's char, see weather it can be palindrome.
26. [914. Flip Game](https://www.lintcode.com/problem/flip-game/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/0914-flip-game.py)
27. [1011. Number of Lines To Write String](https://www.lintcode.com/problem/number-of-lines-to-write-string/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/1011-number-of-lines-to-write-string.py)
28. [1013. Unique Morse Code Words](https://www.lintcode.com/problem/unique-morse-code-words/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/1013-unique-morse-code-words.py)
29. [1079. Count Binary Substrings](https://www.lintcode.com/problem/count-binary-substrings/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/1079-count-binary-substrings.py)
30. [1104. Judge Route Circle](https://www.lintcode.com/problem/judge-route-circle/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/1104-judge-route-circle.py)
31. [1173. Reverse Words in a String III](https://www.lintcode.com/problem/reverse-words-in-a-string-iii/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/1173-reverse-words-in-a-string-iii.py)
32. [1193. Detect Capital](https://www.lintcode.com/problem/detect-capital/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/1193-detect-capital.py)
33. [1204. Keyboard Row](https://www.lintcode.com/problem/keyboard-row/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/1204-keyboard-row.py)
34. [1243. Number of Segments in a String](https://www.lintcode.com/problem/number-of-segments-in-a-string)
35. [1266. Find the Difference](https://www.lintcode.com/problem/find-the-difference) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/1266-find-the-difference.py)
36. [1283. Reverse String](https://www.lintcode.com/problem/reverse-string/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/1283-reverse-string.py)
37. [1350. Excel Sheet Column Title](https://www.lintcode.com/problem/excel-sheet-column-title/) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/1350-excel-sheet-column-title.py)
38. [1638. Least Substring](https://www.lintcode.com/problem/least-substring) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/1638-least-substring.py)
39. [1713. Unique Email Addresses](https://www.lintcode.com/problem/unique-email-addresses) [<b>[Solution]<b>](https://github.com/runzezhang/Code-NoteBook/blob/master/lintcode/1713-unique-email-addresses.py)