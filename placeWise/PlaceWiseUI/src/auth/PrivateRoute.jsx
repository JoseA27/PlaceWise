// Este codigo no es funcional, es solo un ejemplo de como se podria implementar PrivateRoute en un proyecto de React

import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import PropTypes from 'prop-types';
import { useAuth } from '../context/AuthContext';

const PrivateRoute = ({ component: Component, ...rest }) => {
    const { currentUser } = useAuth();

    return (
        <Route
            {...rest}
            render={props =>
                currentUser ? (
                    <Component {...props} />
                ) : (
                    <Redirect to="/login" />
                )
            }
        />
    );
};

PrivateRoute.propTypes = {
    component: PropTypes.elementType.isRequired,
};

export default PrivateRoute;