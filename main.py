class Solution {
public boolean isValid(String s) {
Stack < Character > st=new Stack <> ();
boolean res=true;
for (int i=0;i < s.length();i++)
{
char c=s.charAt(i);
if (c == '(' | | c == '{' | | c == '[')
{
st.push(c);
}
else if (c == ')')
{
if (!st.empty() & & st.peek() == '(')
{
st.pop();
}
else
{
res=false;


break;
}
}
else if (c == '}')
{
if (!st.empty() & & st.peek() == '{')
{
st.pop();
}
else
{
res = false;
break;
}
}
else if (c == ']')
{
if (!st.empty() & & st.peek() == '['){
st.pop();
}
else
{
res = false;
break;
}
}

}

if (!st.empty())
{
res=false;

}
return res;
}
}