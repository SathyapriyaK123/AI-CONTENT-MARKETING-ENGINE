"""
User-friendly error messages
"""

ERROR_MESSAGES = {
    "api_key_missing": {
        "message": "API key not configured",
        "solution": "Please add GROQ_API_KEY to your .env file",
        "code": "CONFIG_ERROR",
    },
    "api_connection": {
        "message": "Failed to connect to AI service",
        "solution": "Check your internet connection and API key",
        "code": "CONNECTION_ERROR",
    },
    "rate_limit": {
        "message": "API rate limit exceeded",
        "solution": "Please wait a moment and try again. Free tier has limited requests.",
        "code": "RATE_LIMIT",
    },
    "invalid_input": {
        "message": "Invalid input provided",
        "solution": "Please check your input and try again",
        "code": "VALIDATION_ERROR",
    },
    "generation_failed": {
        "message": "Content generation failed",
        "solution": "Please try again with a different prompt or contact support",
        "code": "GENERATION_ERROR",
    },
    "timeout": {
        "message": "Request timed out",
        "solution": "The request took too long. Try with shorter content or simpler request",
        "code": "TIMEOUT_ERROR",
    },
}


def get_error_response(error_type: str, details: str = None) -> dict:
    """
    Get formatted error response

    Args:
        error_type: Type of error (key from ERROR_MESSAGES)
        details: Additional error details
    """
    error_info = ERROR_MESSAGES.get(
        error_type,
        {
            "message": "An unexpected error occurred",
            "solution": "Please try again or contact support",
            "code": "UNKNOWN_ERROR",
        },
    )

    response = {
        "success": False,
        "error": {
            "message": error_info["message"],
            "solution": error_info["solution"],
            "code": error_info["code"],
        },
    }

    if details:
        response["error"]["details"] = details

    return response


def format_validation_error(field: str, issue: str) -> dict:
    """Format validation error"""
    return {
        "success": False,
        "error": {
            "message": f"Validation failed for {field}",
            "issue": issue,
            "code": "VALIDATION_ERROR",
        },
    }
