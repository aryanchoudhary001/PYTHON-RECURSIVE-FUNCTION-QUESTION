#include <stdio.h>

int main() {
    int n, x, i, count = 0;

    printf("Enter size of array: ");
    scanf("%d", &n);

    int arr[n];

    printf("Enter array elements:\n");
    for(i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter element to count: ");
    scanf("%d", &x);

    for(i = 0; i < n; i++) {
        if(arr[i] == x) {
            count++;
        }
    }

    printf("Element appears %d times", count);

    return 0;
}