from user import register_user

class TestRegisterUser:
    
    def test_user_is_registered(self):
        user_data ={
            'first_name': 'rafael',
            'last_name': 'Flores',
            'birthdate': '1992-11-27',
            'gender': 'male',
            'email': 'r.flores@levelup.gt'
        }
        #Act
        message = register_user(**user_data) #knought

        #Assert
        assert message == 'User succesfully registered'
        from user import user_dict
        assert user_dict == user_data
    
    def test_should_raise_an_error_if_geneder_is_incorrect(self):
        user_data = {
            'first_name': 'rafael',
            'last_name': 'Flores',
            'birthdate': '1992-11-27',
            'gender': 'incorrect',
            'email': 'r.flores@levelup.gt'
        }

    def test_should_raise_an_error_if_email_is_incorrect(self):
        with pytest.raises(Exception) as error:
            user_data = {
            'first_name': 'rafael',
            'last_name': 'Flores',
            'birthdate': '1992-11-27',
            'gender': 'incorrect',
            'email': 'r.flores@levelup.gt'
        }

#edge cases 1 error que debe ocurrir si gender trae algun valor no valido
# case 2 el correo debe ser valido