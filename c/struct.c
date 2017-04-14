#include<stdio.h>
#include<string.h>
struct student
{
    char name[20];
    int age;
    int sex;
    int height;
    struct student *next;
};
void showstu(struct student *stu)
{
    struct student *p = stu;
    if(p==NULL)
    {
        printf("no student.\n");
    }
    else
    {
        do{
            printf("studnet:\n");
            printf("\tname:%s.\n",p->name);
            printf("\tage:%d.\n",p->age);
            if(p->sex)
            {
                printf("\tman.\n");
            }
            else
            {
                printf("\twoman.\n");
            }
            printf("\theight:%d.\n",p->height);
            p = p->next;
        }while(p!=NULL);
    }
}
void main()
{
    struct student *stu,tmp;
    stu = &tmp;
    strcpy(tmp.name,"zhangs");
    tmp.age = 30;
    tmp.sex = 1;
    tmp.height = 160;
    tmp.next = NULL;
    showstu(stu);
}
