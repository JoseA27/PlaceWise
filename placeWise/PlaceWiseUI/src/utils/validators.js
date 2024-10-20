// Este codigo no es funcional, es solo un ejemplo de como se podria implementar validators para un proyecto de React
// validators.js

/**
 * Checks if the given value is a valid email address.
 * @param {string} email - The email address to validate.
 * @returns {boolean} True if the email is valid, false otherwise.
 */
export function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Checks if the given value is a valid phone number.
 * @param {string} phoneNumber - The phone number to validate.
 * @returns {boolean} True if the phone number is valid, false otherwise.
 */
export function isValidPhoneNumber(phoneNumber) {
    const phoneRegex = /^\+?[1-9]\d{1,14}$/;
    return phoneRegex.test(phoneNumber);
}

/**
 * Checks if the given value is a non-empty string.
 * @param {string} value - The string to validate.
 * @returns {boolean} True if the string is non-empty, false otherwise.
 */
export function isNonEmptyString(value) {
    return typeof value === 'string' && value.trim().length > 0;
}

/**
 * Checks if the given value is a valid URL.
 * @param {string} url - The URL to validate.
 * @returns {boolean} True if the URL is valid, false otherwise.
 */
export function isValidURL(url) {
    try {
        new URL(url);
        return true;
    } catch (_) {
        return false;
    }
}