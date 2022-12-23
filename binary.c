#include <stdio.h>
#include <string.h>
#include <stdlib.h>
// Usage: ./binary or ./binary [input file]

int main(int argc, char const *argv[]){

    char buff[5];
    if(argc == 2){
        // Read first line from input file
        FILE* fp = fopen(argv[1], "r");
        fgets(buff, 5, fp);
        buff[4] = '\0';
        printf("Read first line \"%s\" from input file.\n", buff);
    }else{
        printf("Enter abcd: ");
        scanf("%4s", buff);
        buff[4] = '\0';
    }
    

    if(strcmp(buff, "abcd") == 0){
        printf("Continuing\n");
    }else{
        printf("Exiting\n");
        exit(0);
    }

    printf("Enter efgh: ");
    scanf("%4s", buff);
    buff[4] = '\0';

    if(strcmp(buff, "abcd") == 0){
        printf("Exiting\n");
    }else{
        printf("You win!\n");
        exit(0);
    }
}