#include <stdio.h>	/*library for input output and files (printf, fopen, fread, fgets)*/
#include <stdlib.h>	/*library required to use the malloc function*/
#include <string.h>	/*library for string manipulations incl. strlen, strcmp*/

/*argc contains the count of arguments supplied to the command line, including the commands itself
*argv contains the lest of arguments following the command, the first argument is the second possition of the array. location 1.
*argv is an array of strings, which themselves are an array of characters.
*the '*' shows it is an array or pointer (they are interchangable)*/
int main(int argc, char**argv)
{
	char * raw;	/*uninitialise pointers to output array*/
	int outlen;	/**length of output array*/
	int inlen;	/*contains the length of input string from command line argument*/
	int argid;	//the postion in argv to find the hext string
	//print usage instructions
	if(argc<2){
		printf("hex2raw [-h|-d] HEXSTRING\n \
				Outputs the binary string (non-printing) for given hex string.\n \
				HEXSTRING\tHexadecimal string 0-9A-F only.\n \
				Use -h to print human readable binary string.\n \
				Use -d to print decimal value of hex string.(requires even length string.)");
		return 0;
	}
	/*get the length of the hex string. argv[1] is first argument.*/
	if(*argv[1]!='-'){
		argid=1;
		inlen=strlen(argv[1]);
	} else {
		argid=2;
		inlen=strlen(argv[2]);
	}

	/*assign memmory for output array.
	*if converting to binary array will be 4 times longer than hex string.
	*if converting to decimal array will be half as long*/
	if (inlen%2==0 && argc==3 && strcmp(*(argv+1),"-d")==0){
		outlen=inlen/2;
		raw=(char *)malloc(outlen+1);	/*extra 1 byte for null terminating string*/
		if (raw==NULL){printf("malloc failed\n");return 1;}
		raw[outlen+inlen%2]=0x0;
	} else {
		outlen=4*inlen;
		raw=(char *)malloc(outlen+1);
		if (raw==NULL){printf("malloc failed\n");return 1;}
		raw[outlen]=0x0;
	}
	/*step 1. convert each letter in the hex string to its decimal value(A-F being 10-15) by subtracting the ascii offset. (refer to ascii codes)*/
	for (int i=0;i<inlen;i++){
		char tmp=0x0;
		/*note the 0x infront of a number meanse it is hexadecimal notation, otherwise it is ordinary decimal.
		*if the ascii value is 48 to 57 subtract 48 (digits 0 through 9)*/
		if (*(argv[argid]+i)>=0x30 && *(argv[argid]+i)<=0x39){
			tmp=*(argv[argid]+i)-0x30;
		}

		/*else if ascii value is 65 to 70 subtract 55 (Letters A throuh F)*/
		else if(*(argv[argid]+i)>=0x41 && *(argv[argid]+i)<=0x46){
			tmp=*(argv[argid]+i)-0x37;
		}

		/*else if ascii value is 97 to 102 subract 87 (Letters a through f)*/
		else if(*(argv[argid]+i)>=0x61 && *(argv[argid]+i)<=0x66){
			tmp=*(argv[argid]+i)-0x57;
		}
		else{
			printf("Error: Not A Hex Character"); return 2;
		}
		
		/*step 2. if -d for decimal value is specified each pair or hex characters need to be shifted and added to produce: 0x41=4x16+1
		*even numbered character in the hex string are the MSB of a pair of hex characters*/
		if(argc==3 && strcmp(*(argv+2), "-d")==0){
			if (i%2==0){
				raw[i/2]=tmp<<4;
			}else{
				raw[i/2]+=tmp;
			}
		}else{
			/*step 3. shift right 0,1,2,3,times and combine with mask 0x1 to obtain individual bits and put them in array
			*each hexa decimal character comprises 4 bits (0 to F)*/
			for(int j=0;j<4;j++){	
				raw[i*4+j]=((tmp>>(3-j))&0x1);
				/*if -h specified add 0x30 (48) to obtain the offset for printable ascii 0 character. (see ascii codes)*/
		       		if(argc==3 && strcmp(*(argv+2),"-h")==0){
					raw[i*4+j]+=0x30;
		       		}
			}
		}
	
	}
	for(int i=0;i<outlen;i++){printf("%c",raw[i]);}
	return 0;
}
