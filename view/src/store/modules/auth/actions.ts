interface AuthPayload {
    email: string;
    password: string;
    fullname: string;
    phone: string;
    mode: string;
    date_of_birth: string;
    role: string;
}

export default {

    async auth(context: any, payload: AuthPayload) {
        const mode = payload.mode;
        let apiUrl = await context.rootGetters.getApiUrl;
        console.log(apiUrl);
        
        if (mode === 'register') {
            apiUrl += 'register';
        } else if(mode === 'login') {
            apiUrl += 'login';
        }

        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                email: payload.email,
                password: payload.password,
                fullname: payload.fullname,
                date_of_birth: payload.date_of_birth,
                phone: payload.phone,
            })
        })

        const responseData = await response.json();

        if(!response.ok) {
            const error = new Error('Có lỗi xảy ra trong quá trình đăng ký');
            throw error;
        }

        console.log('handle auth');
        

        localStorage.setItem('token', responseData.jwtToken);
        context.commit('setUser', {
            token: responseData.jwtToken,
            userId: responseData.user.id
        });

    }
}