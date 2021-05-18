/*
 * Ory APIs
 *
 * Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 
 *
 * The version of the OpenAPI document: v0.0.1-alpha.3
 * Contact: support@ory.sh
 * Generated by: https://openapi-generator.tech
 */

/// LoginViaApiResponse : The Response for Login Flows via API



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct LoginViaApiResponse {
    #[serde(rename = "session")]
    pub session: Box<crate::models::Session>,
    /// The Session Token  A session token is equivalent to a session cookie, but it can be sent in the HTTP Authorization Header:  Authorization: bearer ${session-token}  The session token is only issued for API flows, not for Browser flows!
    #[serde(rename = "session_token")]
    pub session_token: String,
}

impl LoginViaApiResponse {
    /// The Response for Login Flows via API
    pub fn new(session: crate::models::Session, session_token: String) -> LoginViaApiResponse {
        LoginViaApiResponse {
            session: Box::new(session),
            session_token,
        }
    }
}


