"""
# Lab: Read in data, store, manipulate and output new data to a file

In this lab you'll read the contents of a file and then write the contents to another file.  
You'll store the contents of a file into a list so that it can be accessed in different ways. 

## There are two objectives of this activity: 
1. Create a function for reading in a file

2. Create a function for writing files.

## Exercise Instructions:  
1. Check that the `sampletext.txt` and `file_ops.py` files exist and are present inside the project folder.   
   You can run the `file_ops.py` file by opening a terminal and executing the following command:
    ```
    python3 file_ops.py 
    ```

2. Complete the `read_file()` function to read in the sampletext.txt file using the `open` function and return the entire contents of the file. 

3. Complete the `read_file_into_line()` function so that it returns a data structure of all the contents of the file in a line-by-line sequential order.

4. Fill in the `write_first_line_to_file()` that accepts two arguments. This should write only the first line of the file contents into the given output file.   

    - **Argument 1:** The contents of a file to be written
    - **Argument 2:** The name of an output file.

5. Complete the `read_even_numbered_lines()` to return a list of the even-numbered lines of a file (2, 4, 6, etc.) 

6. Fill in the `read_file_in_reverse()` function to return a list of the lines of a file in reverse order. 


"""




def read_file(file_name):
    """ Reads in a file.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable using the File read()
           function
        2. Print the contents of the file
        3. Return the contents of the file

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
    ### WRITE SOLUTION HERE
    with open(file_name, 'r') as f:
        contents=f.read()

    return contents
    
    
    
    raise NotImplementedError()

def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list

    [IMPLEMENT ME]
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    ### WRITE SOLUTION HERE
    List=[]
    with open( file_name, 'r') as file :
        List=file.readlines()
    return List

    

    raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.

    [IMPLEMENT ME]
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    ### WRITE SOLUTION HERE
    file_contents=file_contents.split('\n')
    li=file_contents[0]  
    with open(output_filename, 'w') as f:
        c=f.write(li)
    return c
   

    raise NotImplementedError()


def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
    ### WRITE SOLUTION HERE
    List=[]
    with open(file_name , 'r') as f :
        lines=f.readlines()
        i=1
        for line in lines :
            if i%2==0:
                List.append(line)
            i+=1
    return List
    


    raise NotImplementedError()

def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    ### WRITE SOLUTION HERE
    with open( file_name,'r') as f :
        List=f.readlines()
    return List[::-1]
    
    
    raise NotImplementedError()

'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()
