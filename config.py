import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    STRIPE_PUBLIC_KEY = 'ypk_test_51RJCnKPLKdDMzpK8pIs4mfp5oP187jgywxUVnOrr5TIyJKL1olHKCYgn0tUu3HSuIHIMdhzNM6Lhzim385nNhaBy00SPwxya85'
    STRIPE_SECRET_KEY = 'sk_test_51RJCnKPLKdDMzpK89oxGEccXI9OVJ4VO2LOu4KEOjh64Ftzj78ScAA7my9b4otiSHjjEu1XASzSMyHHA9FVLStp900CLqPaDuc'
