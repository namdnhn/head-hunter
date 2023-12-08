export default {
	async getCvByUserId(context: any, userId: string) {
		let apiUrl = await context.rootGetters.getApiUrl;
		apiUrl += `cv/user/${userId}`;

		const response = await fetch(apiUrl, {
			method: "GET",
			headers: {
				"Content-Type": "application/json",
			},
		});

		const responseData = await response.json();
		if (!response.ok) {
			const error = new Error(
				responseData.message || "Failed to fetch cv."
			);
			throw error;
		}

		context.commit("setCv", responseData);

        return responseData;
        

	},
};
