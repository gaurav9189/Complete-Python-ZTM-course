if __name__ == '__main__':
    # Whichever file is executed becomes the __main__ file, the other files will be called with their names
    # such as modules_172(filename) and shopping.shop(pkg.filename)
    import modules_172
    import shopping.shop
    print(modules_172.guess_game(10))
    print(shopping.shop.add_cart('apple'))
