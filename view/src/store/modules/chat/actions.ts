export default {
    async getCompanies() {
        let apiUrl = 'http://localhost:3000/companies'

        const response = await fetch(apiUrl, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })

        const responseData = await response.json()

        if (!response.ok) {
            const error = new Error(
                responseData.message || 'Failed to fetch companies.'
            )
            throw error
        }

        return responseData
    },
    async getCompany(_: any, id: any) {
        let apiUrl = 'http://localhost:3000/companies/' + id

        const response = await fetch(apiUrl, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })

        const responseData = await response.json()

        if (!response.ok) {
            const error = new Error(
                responseData.message || 'Failed to fetch company.'
            )
            throw error
        }

        return responseData
    }
}