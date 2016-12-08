# Webbed
Allows the execution of python code within any file.

# Use from command line

```html
<html>
    <body>
        <p>The following is executed using python</p>
        <?python
            hello = 'Hello world!'
            print('<p>' + hello + '</p>', end='')
        ?>
    </body>
</html>
```

The above html code will transform into the following
```html
<html>
    <body>
        <p>The following is executed using python</p>
        <p>Hello world!</p>
    </body>
</html>
```

## Executing from command line
 
```sh
python -m webbed path_to_file
```

## Executing from python script

```python
from webbed import webbed
formated_text = webbed('path_to_file')
```

Executing from a python script also allows to import and export global variables from and to
the file
```python
from webbed import webbed
foo = 'bar'
# Give the file access to the variable 'foo'
global_variables = {'foo': foo}  

formated_text = webbed('path_to_file', global_variables)

# Access the global variable "hello" from the file
print(global_variables['hello'])  # will output 'Hello world!'
```
