// Este codigo no es funcional, es solo un ejemplo de como se podria implementar un hook para subir archivos a un servidor

import { useState } from 'react';

const useForm = (initialValues, validate) => {
    const [values, setValues] = useState(initialValues);
    const [errors, setErrors] = useState({});

    const handleChange = (event) => {
        const { name, value } = event.target;
        setValues({
            ...values,
            [name]: value,
        });

        if (validate) {
            const validationErrors = validate(values);
            setErrors(validationErrors);
        }
    };

    const handleSubmit = (event, callback) => {
        event.preventDefault();
        if (validate) {
            const validationErrors = validate(values);
            setErrors(validationErrors);
            if (Object.keys(validationErrors).length === 0) {
                callback();
            }
        } else {
            callback();
        }
    };

    return {
        values,
        errors,
        handleChange,
        handleSubmit,
    };
};

export default useForm;