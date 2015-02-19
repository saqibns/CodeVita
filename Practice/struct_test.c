typedef struct my_variable_is_this
{
    int a;
    char* str;
} my;

void details(my st)
{
    printf("%d\n", st.a);
    printf("%s\n", st.str);
}

int main()
{
    my s1;
    s1.a = 2;
    s1.str = "Saqib";
    details(s1);
    return 0;
}
