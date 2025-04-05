export const BASE_URL = 'http://localhost:5000'

// API PATHS FROM SERVER
export const API_PATHS= {
    AUTH: {
        LOGIN: '/auth/login',
        SIGNUP: '/auth/register',
    },
    PATIENT: {
        GET: (patientId) => `/patient/${patientId}`,
        UPDATE: (patientId) => `/patient/update/${patientId}`
    }
}