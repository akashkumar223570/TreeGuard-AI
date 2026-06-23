from services.history import save_scan
from services.history import get_history

save_scan({
    "disease":"Tomato_Leaf_Mold",
    "confidence":95.45
})

print(
    get_history()
)