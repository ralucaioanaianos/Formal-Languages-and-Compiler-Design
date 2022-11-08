package ro.ubb.lab11.core.service;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import ro.ubb.lab11.core.exceptions.MagicException;
import ro.ubb.lab11.core.model.Airplane;
import ro.ubb.lab11.core.model.validators.AirplaneValidator;
import ro.ubb.lab11.core.repository.IAirplaneRepository;

import java.util.List;

@Service
public class AirplaneServiceImpl implements IAirplaneService{
    public static final Logger logger = LoggerFactory.getLogger((AirplaneServiceImpl.class));

    @Autowired
    private IAirplaneRepository airplaneRepo;
    @Autowired
    private AirplaneValidator validator;
    //@Autowired
    //private ICastedSpellRepository CastedSpellRepository;
    //@Autowired
    //private IPetRepository petRepository;

    @Override
    public List<Airplane> getAllAirplanes() {
        logger.trace("Get all Airplanes method: ");
        List<Airplane> airplanes = airplaneRepo.findAll();
        logger.trace("allAirplanes: " + airplanes);
        return airplanes;
    }

    @Override
    public Airplane addAirplane(String model, int capacity, String registration, int fabricationYear) {
        /*logger.trace("addAirplane - name: " + name + " - age: " + age + " - pet: " + pet);
        Airplane newAirplane = new Airplane(name, age, pet);
        validator.validate(newAirplane);
        var Airplane = AirplaneRepo.save(newAirplane);
        logger.trace("AddAirplane - method finished");
        return Airplane;*/
        logger.trace("addAirplane - model: " + model + " - capacity: " + capacity + " - registration: " + registration + " - fabricationYear: " + fabricationYear);
        Airplane newAirplane = new Airplane(model, capacity, registration, fabricationYear);
        validator.validate(newAirplane);
        var airplane = airplaneRepo.save(newAirplane);
        logger.trace("AddAirplane - method finished");
        return airplane;
    }

    @Override
    public void deleteAirplane(Long id) {
        /*logger.trace("deleteAirplane - method entered - id: " + id);
        CastedSpellRepository.findAll().stream()
                .filter(castedSpell -> castedSpell.getAirplaneId().equals(id))
                .findAny()
                .ifPresent(castedSpell -> {
                    throw new MagicException("The Airplane has a casted spell!");
                });
        petRepository.findAll().stream()
                .filter(pet -> pet.getWid().equals(id))
                .findAny()
                .ifPresent(pet -> {
                    throw new MagicException("The Airplane has a pet!");
                });

        AirplaneRepo.findById(id).ifPresentOrElse((Airplane) -> AirplaneRepo.deleteById(id), () ->{
            throw new MagicException("Airplane does not exist!");
        });
        logger.trace("deleteAirplane - method finished");*/
        logger.trace("deleteAirplane - method entered - id: " + id);
        // TO DO: RELATIILE CU CELELALTE TABELe
        airplaneRepo.findById(id).ifPresentOrElse((airplane) -> airplaneRepo.deleteById(id), () -> {
            throw  new MagicException("airplane does not exist!");
        });
        logger.trace("deleteAirplane - method finished");
    }

    @Override
    @Transactional
    public Airplane updateAirplane(Long id, String model, int capacity, String registration, int fabricationYear) {
        /*logger.trace("updateAirplane - id: " + id + " - name: " + name + " - age: " + age + " - pet: " + pet);
        Airplane Airplane = new Airplane(name, age, pet);
        Airplane.setId(id);
        validator.validate(Airplane);
        AirplaneRepo.findById(id).ifPresentOrElse((Airplane1) -> {
            Airplane1.setName(name);
            Airplane1.setAge(age);
            Airplane1.setPet(pet);
        }, () -> {
            throw new MagicException("Airplane does not exist!");
        });
        logger.trace("updateAirplane - method finished");
        return Airplane;*/
        logger.trace("updateAirplane - id: " + id + " - model: " + model + " - capacity" + capacity + " - registration" + registration + " - fabricationYear" + fabricationYear);
        Airplane airplane = new Airplane(model, capacity, registration, fabricationYear);
        airplane.setId(id);
        validator.validate(airplane);
        airplaneRepo.findById(id).ifPresentOrElse((airplane1) -> {
            airplane1.setModel(model);
            airplane1.setCapacity(capacity);
            airplane1.setRegistration(registration);
            airplane1.setFabricationYear(fabricationYear);
        }, () -> {
            throw new MagicException("airplane does not exist!");
        });
        logger.trace("updateAirplane - method finished!");
        return airplane;
    }

    @Override
    public List<Airplane> findAirplanesByModel(String model) {
        /*logger.trace("findAirplanesByName - name = {}", name);
        var result = AirplaneRepo.findAllByName(name);
        logger.trace("findAirplanesByName - method finished - result = {}", result);
        return result;*/
        logger.trace("findAirplanesByModel - name = {}", model);
        var result = airplaneRepo.findAllByModel(model);
        logger.trace("findAirplanesByModel - method finished - result = {}", result);
        return result;
    }

    @Override
    public List<Airplane> findAllByOrderByAgeAsc() {
        return airplaneRepo.findAllByOrderByAgeAsc();
    }
}
