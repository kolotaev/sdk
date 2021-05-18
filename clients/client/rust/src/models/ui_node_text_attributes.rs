/*
 * Ory APIs
 *
 * Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 
 *
 * The version of the OpenAPI document: v0.0.1-alpha.3
 * Contact: support@ory.sh
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct UiNodeTextAttributes {
    #[serde(rename = "text")]
    pub text: Box<crate::models::UiText>,
}

impl UiNodeTextAttributes {
    pub fn new(text: crate::models::UiText) -> UiNodeTextAttributes {
        UiNodeTextAttributes {
            text: Box::new(text),
        }
    }
}


