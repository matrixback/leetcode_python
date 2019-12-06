```go
func isOneBitCharacter(bits []int) bool {
    i := 0
    length := len(bits)
    for i < length {
        if bits[i] == 0 {
            i++
            if i == length {
                return true
            }
        } else {
            i = i + 2
            if i == length {
                return false
            }
        }
    }
    return false
}
```
