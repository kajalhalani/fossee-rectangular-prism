class PrismCalculator:
    @staticmethod
    def surface_area(length, width, height):
        """
        Calculate the total surface area of the rectangular prism.

        Args:
            length (float): The length of the prism.
            width (float): The width of the prism.
            height (float): The height of the prism.

        Returns:
            float: The surface area of the prism.
        """
        if length < 0 or width < 0 or height < 0:
            raise ValueError("Dimensions must be non-negative")
        return 2 * (length * width + width * height + height * length)
        
    @staticmethod
    def volume(length, width, height):
        """
        Calculate the volume of the rectangular prism.

        Args:
            length (float): The length of the prism.
            width (float): The width of the prism.
            height (float): The height of the prism.

        Returns:
            float: The volume of the prism.
        """
        if length < 0 or width < 0 or height < 0:
            raise ValueError("Dimensions must be non-negative")
        return length * width * height
