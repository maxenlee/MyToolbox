def pyrator(function):
    """
    A function decorator that converts regular docstrings into pirate speak.

    Args:
        function (function): The function with a regular docstring.

    Returns:
        function: The function with a pirate-style docstring.
    
    Example usage:
        
        @pirate_docstring
        def add(a, b):
        |  |  |
        Adds two numbers together.
    
        Args:
            a (int): The first number.
            b (int): The second number.
    
        Returns:
            int: The sum of the two numbers.
        |  |  |
        
        return a + b
        
    
        # Test the function
        print(help(add))
    """
    pirate_phrases = {
        'Args:': 'Mateys:',
        'Returns:': 'Returns ye booty:',
        'Examples:': 'Examples o\' use:',
        'Raises:': 'Watch out fer:',
        'See Also:': 'Ahoy, see also:',
        'References:': 'References to treasures:',
        'Note:': 'Arr, listen up:',
        'Warning:': 'Avast, ye be warned:'
    }

    # Get the original docstring
    original_docstring = function.__doc__

    if original_docstring:
        # Convert the docstring into pirate speak
        for key, value in pirate_phrases.items():
            original_docstring = original_docstring.replace(key, value)

    # Update the function's docstring
    function.__doc__ = original_docstring

    return function



