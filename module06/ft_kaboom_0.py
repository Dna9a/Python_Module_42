import alchemy.grimoire.light_spellbook as light_spellbook

spell_result = light_spellbook.light_spell_record(
    "Fantasy",
    "Earth, wind and fire",
)

print("=== Kaboom 0 ===")
print("Using grimoire module directly")
print("Testing record light spell: " f"{spell_result}\n")
