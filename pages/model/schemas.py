get_create_task = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "data": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "text": {
          "type": "string"
        },
        "notes": {
          "type": "string"
        },
        "tags": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "value": {
          "type": "number"
        },
        "priority": {
          "type": "number"
        },
        "attribute": {
          "type": "string"
        },
        "challenge": {
          "type": "object",
          "properties": {},
          "required": []
        },
        "group": {
          "type": "object",
          "properties": {
            "completedBy": {
              "type": "object",
              "properties": {},
              "required": []
            },
            "assignedUsers": {
              "type": "array",
              "items": {}
            }
          },
          "required": [
            "completedBy",
            "assignedUsers"
          ]
        },
        "reminders": {
          "type": "array",
          "items": {}
        },
        "byHabitica": {
          "type": "boolean"
        },
        "_id": {
          "type": "string"
        },
        "completed": {
          "type": "boolean"
        },
        "collapseChecklist": {
          "type": "boolean"
        },
        "checklist": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "completed": {
                "type": "boolean"
              },
              "text": {
                "type": "string"
              },
              "id": {
                "type": "string"
              }
            },
            "required": [
              "completed",
              "text",
              "id"
            ]
          }
        },
        "createdAt": {
          "type": "string"
        },
        "updatedAt": {
          "type": "string"
        },
        "userId": {
          "type": "string"
        },
        "id": {
          "type": "string"
        }
      },
      "required": [
        "type",
        "text",
        "notes",
        "tags",
        "value",
        "priority",
        "attribute",
        "challenge",
        "group",
        "reminders",
        "byHabitica",
        "_id",
        "completed",
        "collapseChecklist",
        "checklist",
        "createdAt",
        "updatedAt",
        "userId",
        "id"
      ]
    },
    "notifications": {
      "type": "array",
      "items": {}
    },
    "userV": {
      "type": "number"
    },
    "appVersion": {
      "type": "string"
    }
  },
  "required": [
    "success",
    "data",
    "notifications",
    "userV",
    "appVersion"
  ]
}
get_tasks = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "_id": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "text": {
            "type": "string"
          },
          "notes": {
            "type": "string"
          },
          "tags": {
            "type": "array",
            "items": {}
          },
          "value": {
            "type": "number"
          },
          "priority": {
            "type": "number"
          },
          "attribute": {
            "type": "string"
          },
          "challenge": {
            "type": "object",
            "properties": {},
            "required": []
          },
          "group": {
            "type": "object",
            "properties": {
              "completedBy": {
                "type": "object",
                "properties": {},
                "required": []
              },
              "assignedUsers": {
                "type": "array",
                "items": {}
              }
            },
            "required": [
              "completedBy",
              "assignedUsers"
            ]
          },
          "reminders": {
            "type": "array",
            "items": {}
          },
          "byHabitica": {
            "type": "boolean"
          },
          "completed": {
            "type": "boolean"
          },
          "collapseChecklist": {
            "type": "boolean"
          },
          "checklist": {
            "type": "array",
            "items": {}
          },
          "createdAt": {
            "type": "string"
          },
          "updatedAt": {
            "type": "string"
          },
          "userId": {
            "type": "string"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "_id",
          "type",
          "text",
          "notes",
          "tags",
          "value",
          "priority",
          "attribute",
          "challenge",
          "group",
          "reminders",
          "byHabitica",
          "createdAt",
          "updatedAt",
          "userId",
          "id"
        ]
      }
    },
    "notifications": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string"
          },
          "data": {
            "type": "object",
            "properties": {
              "title": {
                "type": "string"
              }
            },
            "required": [
              "title"
            ]
          },
          "seen": {
            "type": "boolean"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "data",
          "seen",
          "id"
        ]
      }
    },
    "userV": {
      "type": "number"
    },
    "appVersion": {
      "type": "string"
    }
  },
  "required": [
    "success",
    "data",
    "notifications",
    "userV",
    "appVersion"
  ]
}