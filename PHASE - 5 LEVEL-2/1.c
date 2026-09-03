#include<stdio.h>
int main()
{
    int students,subjects;
    printf("Enter number of students: ");
    scanf("%d",&students);
    printf("Enter number of subjects: ");
    scanf("%d",&subjects);
    int marks[students][subjects];
    printf("\nEnter marks:\n");
    for(int i=0;i<students;i++)
    {
        for(int j=0;j<subjects;j++)
        {
            printf("Student %d Subject %d marks[%d][%d] = ",i+1,j+1,i,j);
            scanf("%d",&marks[i][j]);
        }
    }
    printf("\nMarks Matrix:\n");

    for(int i=0;i<students;i++)
    {
        for(int j=0;j<subjects;j++)
        {
            printf("%d ",marks[i][j]);
        }
        printf("\n");
    }
    printf("\nStudent Total and Average:\n");
    for(int i=0;i<students;i++)
    {
        int total=0;
        for(int j=0;j<subjects;j++)
        {
            total+=marks[i][j];
        }
        printf("Student %d Total = %d\n",i+1,total);
        printf("Student %d Average = %.2f\n",i+1,(float)total/subjects);
    }
    int highest=marks[0][0];
    for(int i=0;i<students;i++)
    {
        for(int j=0;j<subjects;j++)
        {
            if(marks[i][j]>highest)
            {
                highest=marks[i][j];
            }
        }
    }
    printf("\nHighest Mark = %d\n",highest);
    printf("\nSubject Totals:\n");
    for(int j=0;j<subjects;j++)
    {
        int total=0;
        for(int i=0;i<students;i++)
        {
            total+=marks[i][j];
        }
        printf("Subject %d Total = %d\n",j+1,total);
    }
    return 0;
}