#include <stdio.h>

int main() {
    int n, x, i;

    printf("Enter size of array: ");
    scanf("%d", &n);

    int arr[n];

    printf("Enter elements:\n");
    for(i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter element to search: ");
    scanf("%d", &x);

    int found = 0;
    int count = 0;
    int first = -1;
    int last = -1;

    for(i = 0; i < n; i++) {
        if(arr[i] == x) {
            found = 1;
            count++;

            if(first == -1) {
                first = i;
            }

            last = i;
        }
    }

    // 1. Check existence
    if(found)
        printf("Element exists\n");
    else
        printf("Element does not exist\n");

    // 2. Count occurrences
    printf("Count = %d\n", count);

    // 3. First occurrence
    if(first != -1)
        printf("First occurrence index = %d\n", first);
    else
        printf("First occurrence not found\n");

    // 4. Last occurrence
    if(last != -1)
        printf("Last occurrence index = %d\n", last);
    else
        printf("Last occurrence not found\n");

    return 0;
}